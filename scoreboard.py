from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score_data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.goto(0, 145)
        self.display_score()

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,-25)
    #     self.write("Game Over", False, align='center', font=("Courier", 40, 'normal'))

    def victory(self):
        self.clear()
        self.goto(0, -25)
        self.write("Victory!", False, align='center', font=("Courier", 50, 'normal'))
