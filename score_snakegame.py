from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("my_file.txt" ,"r") as file:
            self.highscore =int( file.read())
        self.goto(x=-20, y=270)
        self.color("White")
        self.hideturtle()
        self.penup()
        self.write(f"Score:{self.score}  High Score : {self.highscore}", align="center",
                   font=("Arial", 10, "normal"))

    def add_score(self):
        self.score =self.score + 1
        # self.goto(x=-20, y=270)
        # self.color("White")
        # self.hideturtle()
        # self.penup()

        self.clear()
        self.write(f"Score:{self.score} High Score : {self.highscore}", align="center",
          font=("Arial", 8, "normal"))

    def game_reset(self):
        # self.goto(x=-20, y=270)
        # self.color("White")
        if self.score > self.highscore:
            self.highscore = self.score
            with open("my_file.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} High Score : {self.highscore}", align="center",
                   font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center",
                   font=("Arial", 13, "bold"))
