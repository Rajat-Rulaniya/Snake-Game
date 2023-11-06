import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from boundary import Boundary

food = Food()
screen = t.Screen()
screen.setup(width=750, height=450)
screen.bgcolor('gray10')
screen.title("Snake Game ~Rajat Rulaniya")
screen.tracer(0)

snake = Snake()
screen.listen()
is_game_on = True
scoreboard = ScoreBoard()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)
game_boundary = Boundary()

while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    for segment in snake.turtles[1:len(snake.turtles)]:

        if snake.face.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
            time.sleep(0.7)
            # is_game_on = False
            # scoreboard.game_over()
            break

    if snake.face.distance(food) < 21:
        food.food_eaten()
        snake.extend_snake()
        scoreboard.increase_score()
        scoreboard.display_score()

    # if scoreboard.score >= 10:
    #     is_game_on = False
    #     scoreboard.victory()

    if snake.face.xcor() > 340 or snake.face.xcor() < -340 or snake.face.ycor() > 190 or snake.face.ycor() < -190:
        scoreboard.reset_score()
        snake.reset_snake()
        time.sleep(0.7)
        # is_game_on = False
        # scoreboard.game_over()

screen.exitonclick()
