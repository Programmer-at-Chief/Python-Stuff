import turtle
import random


class Pong:
    def __init__(self):
        self.play_ball=turtle.Turtle()
        self.play_ball.speed(180)
    def mid_line(self):
        interface=turtle.Turtle()
        interface.speed(10)
        interface.color("white")
        interface.hideturtle()
        interface.up()
        interface.lt(90)
        interface.fd(400)
        interface.pensize(10)
        while(interface.distance((0,-400))>10):
            interface.down()
            interface.bk(20)
            interface.up()
            interface.bk(20)

    def create_paddle_left(self):
        self.paddle_left=turtle.Turtle()
        self.paddle_left.shape("square")
        self.paddle_left.up()
        self.paddle_left.speed(30)
        self.paddle_left.goto(-570,0)
        self.paddle_left.color("white")
        self.paddle_left.shapesize(stretch_wid=1,stretch_len=5)
        self.paddle_left.lt(90)

    def create_paddle_right(self):
        self.paddle_right=turtle.Turtle()
        self.paddle_right.shape("square")
        self.paddle_right.up()
        self.paddle_right.speed(30)
        self.paddle_right.goto(570,0)
        self.paddle_right.color("white")
        self.paddle_right.shapesize(stretch_wid=1,stretch_len=5)
        self.paddle_right.rt(90)
    def left_paddle_up(self):
        if (self.paddle_left.ycor()<350):
            self.paddle_left.goto(-570,self.paddle_left.ycor()+50)
    def left_paddle_down(self):
        if (self.paddle_left.ycor()>-350):
            self.paddle_left.goto(-570,self.paddle_left.ycor()-50)
    def right_paddle_up(self):
        if (self.paddle_right.ycor()<350):
            self.paddle_right.goto(570,self.paddle_right.ycor()+50)
    def right_paddle_down(self):
        if (self.paddle_right.ycor()>-350):
            self.paddle_right.goto(570,self.paddle_right.ycor()-50)

    def ball(self):
        self.play_ball.up()
        self.play_ball.color("blue")
        self.play_ball.shape("circle")
        self.play_ball.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=None)


