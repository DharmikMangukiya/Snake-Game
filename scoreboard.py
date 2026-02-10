from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")
FONT_SMALL = ("Arial", 12, "normal")
SCOREBOARD_POSITION = (0, 270)
HIGH_SCORE_FILE = "high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.color("#00FF00")  # Bright green text
        self.write(f"Score: {self.score}  |  Best: {self.high_score}", 
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("#FF4444")  # Bright red
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 36, "bold"))
        self.goto(0, -40)
        self.color("#FFFFFF")
        self.write("Press 'R' to Restart  |  'Q' to Quit", align=ALIGNMENT, font=FONT_SMALL)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()
