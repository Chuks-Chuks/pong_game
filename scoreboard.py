from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.count = 0
        self.goto(position, 280)
        self.clear()
        self.color("white")
        self.write(f"SCORE:{self.count}", False, "center", ("Arial", 12, "bold"))
        self.hideturtle()

    def update_score(self):
        self.count += 1
        self.clear()
        self.color("white")
        self.write(f"SCORE:{self.count}", False, "center", ("Arial", 12, "bold"))
        self.hideturtle()
