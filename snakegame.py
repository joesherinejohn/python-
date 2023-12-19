from turtle import Screen
import random
import time
from snake_joe import Snake
from food_joe import Food
from score_joe import Score

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("Black")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up",fun = snake.up)
screen.onkey(key="Down",fun = snake.down)
screen.onkey(key="Right",fun = snake.right)
screen.onkey(key="Left",fun = snake.left)


screen.update()
food = Food()
score = Score()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.create_food()
        score.add_score()
        snake.extend()

    if snake.head.xcor() >280 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-280:
        # game_on = False
        # score.game_over()
        score.game_reset()
        snake.reset()
        snake.__init__()
    for segments in snake.snake_line[1:]:
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) <10:
            # game_on = False
            # score.game_over()
            score.game_reset()
            snake.reset()
            snake.__init__()

screen.exitonclick()
