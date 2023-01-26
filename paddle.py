from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def up(self):
        my_y = self.ycor()
        my_y += 20
        self.goto(self.xcor(), my_y )

    def down(self):
        my_y = self.ycor()
        my_y -= 20
        self.goto(self.xcor(), my_y )
