from turtle import Turtle
class Snake():
    MOVE_DIST = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180
    def __init__(self):
        self.snake_line = []
        self.x = 0
        self.create_snake()
        self.head = self.snake_line[0]
    def create_snake(self):
        for i in range(3):
            new_object = Turtle()
            new_object.shape("square")
            new_object.color("White")
            new_object.penup()
            new_object.goto(x=self.x, y=0)
            self.x = self.x - 20
            self.snake_line.append(new_object)
    def extend(self):
        new_object = Turtle()
        new_object.shape("square")
        new_object.color("White")
        new_object.penup()
        new_object.goto(self.snake_line[-1].position())
        self.snake_line.append(new_object)

    def move(self):
        for seg in range(len(self.snake_line) - 1, 0, -1):
            new_x = self.snake_line[seg - 1].xcor()
            new_y = self.snake_line[seg - 1].ycor()
            self.snake_line[seg].goto(new_x, new_y)
        self.head.forward(self.MOVE_DIST)
        # self.snake_line[0].left(90)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in range(0, (len(self.snake_line))) :
          self.snake_line[seg].goto(1000,1000)
