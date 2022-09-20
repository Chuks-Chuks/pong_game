from turtle import Turtle
from random import randint


class Ball(Turtle):
    X = 400
    Y = 400
    PACE = 20
    # direction = (x=randint(self.X, self.Y), y = randint(self.X, self.Y))
    angle = randint(0, 270)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_position = 10
        self.y_position = 10
        self.sleep_time = 0.1

    def move(self):
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_position *= -1

    def paddle_bounce(self):
        self.x_position *= -1
        self.sleep_time *= 0.9

    def new_move(self):
        self.goto(0, 0)
        self.sleep_time = 0.1
        self.paddle_bounce()
