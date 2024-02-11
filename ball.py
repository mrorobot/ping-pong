from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(1.4, 1.4, 1)
        self.color("white")
        self.penup()
        self.incx=10
        self.incy=10


    def ball_ini(self):
        self.goto(0,0)
    def ball_move(self):
        new_xcor=self.xcor()+self.incx
        new_ycor=self.ycor()+self.incy
        self.goto(new_xcor, new_ycor )



    def bounce_y(self):
        self.incy*=-1
    def bounce_x(self):
        self.incx*=-1








