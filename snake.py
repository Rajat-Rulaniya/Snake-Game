import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.current_heading = 0
        self.turtles = []
        self.create_snake()
        self.face = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tom = t.Turtle(shape="square")
        tom.color("white")
        tom.penup()
        tom.goto(position)
        self.turtles.append(tom)

    def extend_snake(self):
        self.add_segment(self.turtles[-1].pos())

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_pos = self.turtles[index - 1].pos()
            self.turtles[index].goto(new_pos)

        self.face.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.current_heading != DOWN:
            self.current_heading = UP
            self.face.setheading(self.current_heading)

    def move_right(self):

        if self.current_heading != LEFT:
            self.current_heading = RIGHT
            self.face.setheading(self.current_heading)

    def move_left(self):

        if self.current_heading != RIGHT:
            self.current_heading = LEFT
            self.face.setheading(self.current_heading)

    def move_down(self):

        if self.current_heading != UP:
            self.current_heading = DOWN
            self.face.setheading(self.current_heading)

    def reset_snake(self):
        for snake in self.turtles:
            snake.clear()
            snake.hideturtle()
        self.turtles.clear()
        self.create_snake()
        self.face = self.turtles[0]
