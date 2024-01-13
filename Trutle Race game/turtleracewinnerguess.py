import random
from turtle import Turtle, Screen

user_time = False

screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)

colours=["red","orange", "yellow","green","blue","purple"]
y = -100



turtles = []

for colours in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours)
    new_turtle.goto(x = -200, y = y)
    y = y+50
    turtles.append(new_turtle)

if user_bet:
    user_time = True

while user_time:

    for turtle in turtles :
        if turtle.xcor() >230:
            user_time = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost ! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,20)
        turtle.forward(random_distance)


screen.exitonclick()

