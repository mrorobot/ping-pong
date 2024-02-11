from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.shapesize(7,1.5)
        self.fillcolor("white")
        self.penup()
        self.goto(position)

    def f(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)


    def d(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
