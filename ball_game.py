from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("White")
        self.xmove = 10
        self.ymove = 10
        self.speed_incre = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(x = new_x , y = new_y )


    def bounce_y(self):
        self.ymove *= -1
        self.speed_incre *= 0.9
    def bounce_x(self):
        self.xmove *=-1
        # self.speed_incre *= 0.9
    def reset_position(self):
        self.goto(x= 0,y=0)
        self.speed_incre = 0.1
        self.bounce_x()
