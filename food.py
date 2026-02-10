from turtle import Turtle
import random

# Bright food colors for dark background
FOOD_TYPES = [
    ("#FF6B6B", "#FF0000", 1, "circle"),    # Bright red - 1 point
    ("#FFB347", "#FF8C00", 2, "circle"),    # Bright orange - 2 points  
    ("#FFD700", "#FFA500", 3, "circle"),    # Gold - 3 points
]

GRID_STEP = 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed("fastest")
        self.points = 1
        self.refresh()

    def refresh(self, snake_segments=None):
        """Spawn food at random location, avoiding snake body."""
        while True:
            random_x = random.randint(-13, 13) * GRID_STEP
            random_y = random.randint(-13, 13) * GRID_STEP
            
            if snake_segments:
                spawn_on_snake = False
                for segment in snake_segments:
                    if abs(segment.xcor() - random_x) < 20 and abs(segment.ycor() - random_y) < 20:
                        spawn_on_snake = True
                        break
                if spawn_on_snake:
                    continue
            
            self.goto(random_x, random_y)
            break
        
        food_choice = random.choices(FOOD_TYPES, weights=[70, 25, 5])[0]
        self.shape(food_choice[3])
        self.color(food_choice[1], food_choice[0])
        self.points = food_choice[2]
        self.showturtle()
