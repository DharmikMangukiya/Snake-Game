from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.left_eye = None
        self.right_eye = None
        self.create_snake()
        self.head = self.segments[0]
        self.create_eyes()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        
        if len(self.segments) == 0:
            new_segment.color("#00FF00")  # Bright lime green head
        else:
            new_segment.color("#32CD32")  # Lime green body
        
        self.segments.append(new_segment)

    def create_eyes(self):
        """Create two small eyes on the head."""
        # Left eye
        self.left_eye = Turtle("circle")
        self.left_eye.penup()
        self.left_eye.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.left_eye.color("white")
        
        # Right eye
        self.right_eye = Turtle("circle")
        self.right_eye.penup()
        self.right_eye.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.right_eye.color("white")
        
        self.update_eyes()

    def update_eyes(self):
        """Position eyes based on head direction."""
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        heading = self.head.heading()
        
        # Eye offset based on direction
        if heading == RIGHT:  # 0
            self.left_eye.goto(head_x + 5, head_y + 5)
            self.right_eye.goto(head_x + 5, head_y - 5)
        elif heading == UP:  # 90
            self.left_eye.goto(head_x - 5, head_y + 5)
            self.right_eye.goto(head_x + 5, head_y + 5)
        elif heading == LEFT:  # 180
            self.left_eye.goto(head_x - 5, head_y + 5)
            self.right_eye.goto(head_x - 5, head_y - 5)
        elif heading == DOWN:  # 270
            self.left_eye.goto(head_x + 5, head_y - 5)
            self.right_eye.goto(head_x - 5, head_y - 5)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        if self.left_eye:
            self.left_eye.hideturtle()
        if self.right_eye:
            self.right_eye.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(RIGHT)
        self.create_eyes()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.update_eyes()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
