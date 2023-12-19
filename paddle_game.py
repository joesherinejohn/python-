from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x=0, y=0) :
        super().__init__()
        # self.r_pad = Turtle()
        self.x = x
        self.y = y
        self.create_right_paddle()

    def create_right_paddle(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("White")
        self.goto(x=self.x, y=self.y)

    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
