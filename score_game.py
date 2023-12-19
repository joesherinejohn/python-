from turtle import Turtle

class Line(Turtle):
    def __init__(self, x=0 , y=0):
        super().__init__()
        self.penup()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=0.6, stretch_len= 0.3)
        self.goto(x=x, y=y)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score= 0
        self.r_score = 0
        self.color("White")

    def l_point(self):
        self.l_score +=1
        self.score_print()
    def r_point (self):
        self.r_score +=1
        self.score_print()
    def score_print(self):
        self.clear()
        self.goto(x= -50,y=250)
        self.write(self.l_score,align= "center", font=("Arial",13,"normal"))
        self.goto(x= 50, y=250)
        self.write(self.r_score, align="center", font=("Arial", 13, "normal"))
