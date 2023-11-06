from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-350, -190)
        self.pendown()
        self.goto(350, -190)
        self.goto(350, 190)
        self.goto(-350, 190)
        self.goto(-350, -190)
