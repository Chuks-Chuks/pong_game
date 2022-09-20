from turtle import Turtle
neg_X = -360
pos_X = 360
UP = 90
DOWN = 270


class Pong(Turtle):
    def __init__(self, x_cordinate, y_cordinate):
        super().__init__()
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.create_body()
        self.speed = "fastest"

    def create_body(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x_cordinate, self.y_cordinate)

    def up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)

    def down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
