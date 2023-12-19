from turtle import Turtle,Screen
from paddle22_joe import Paddle
from ball22_joe import Ball
from score22_joe import Line,Score
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.tracer(0)
# 2.Create and move a paddle

r_pad = Paddle(350,0)
l_pad = Paddle(-350,0)

ball = Ball()
score =Score()

line_x =0
line_y = 270
for i  in range (19):
    line =  Line(line_x,line_y)
    line_y -= 30

screen.listen()
screen.onkey(key="Up",fun = r_pad.up)
screen.onkey(key="Down",fun = r_pad.down)
# 3. Create another paddle
screen.onkey(key="w",fun = l_pad.up)
screen.onkey(key="s",fun = l_pad.down)

# 4. Create the ball and make it move


# ball.ball_move()

# 5. detect collision with  wall and bounce
# 6. detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score
# score_A = 0
# score_B = 0
game_on = True
while game_on:
    time.sleep(ball.speed_incre)
    screen.update()
    score.score_print()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_pad) <50 and ball.xcor() >320 or ball.distance(l_pad) <50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor() >380:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()
    # time.sleep(1)

screen.exitonclick()
