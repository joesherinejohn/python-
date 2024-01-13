from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("Blue")
        self.speed("fastest")
        self.create_food()

    def create_food(self):
        self.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))
