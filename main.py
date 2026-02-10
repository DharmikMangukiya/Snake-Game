from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WALL_BOUNDARY = 280
FOOD_COLLISION_DISTANCE = 15
TAIL_COLLISION_DISTANCE = 10
BASE_SPEED = 0.1
SPEED_INCREMENT = 0.005


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#1a1a2e")  # Dark navy blue
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
is_paused = False


def toggle_pause():
    global is_paused
    is_paused = not is_paused


def restart_game():
    global game_is_on, is_paused
    snake.reset()
    scoreboard.reset_score()
    food.refresh(snake.segments)
    game_is_on = True
    is_paused = False


def quit_game():
    screen.bye()


def get_current_speed():
    speed_boost = (scoreboard.score // 5) * SPEED_INCREMENT
    return max(BASE_SPEED - speed_boost, 0.03)


# Key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(toggle_pause, "p")
screen.onkey(toggle_pause, "space")
screen.onkey(restart_game, "r")
screen.onkey(quit_game, "q")

while True:
    screen.update()
    time.sleep(get_current_speed())
    
    if not game_is_on or is_paused:
        continue
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
        for _ in range(food.points):
            scoreboard.increase_score()
        food.refresh(snake.segments)
        snake.extend()

    # Detect collision with wall
    if (snake.head.xcor() > WALL_BOUNDARY or snake.head.xcor() < -WALL_BOUNDARY or 
        snake.head.ycor() > WALL_BOUNDARY or snake.head.ycor() < -WALL_BOUNDARY):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
