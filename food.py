from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.food_eaten()

    def food_eaten(self):
        random_x = random.randint(-320, 320)
        random_y = random.randint(-170, 170)
        self.goto(random_x,random_y)

