import turtle
import setup
import time

class Logic:
    left_points=0
    right_points=0
    timedelay=50
    def __init__(self):
        self.ball_up=True
        self.ball_down=False
        self.ball_right=True
        self.ball_left=False
        self.left_point=turtle.Turtle()
        self.right_point=turtle.Turtle()

    def start(self,ball):
        time.sleep(1/self.timedelay)
        if (self.ball_up and self.ball_right):
            if ball.ycor()<400 and ball.xcor()<600:
                ball.goto(ball.xcor()+10,ball.ycor()+10)
            elif (ball.ycor()<400):
                self.ball_right=False
                self.ball_left=True
            else :
                self.ball_up=False
                self.ball_down=True

        elif (self.ball_up and self.ball_left):
            if ball.ycor()<400 and ball.xcor()>-600:
                ball.goto(ball.xcor()-10,ball.ycor()+10)

            elif (ball.ycor()<400):
                self.ball_left=False
                self.ball_right=True
            else :
                self.ball_up=False
                self.ball_down=True
        elif (self.ball_down and self.ball_right):
            if ball.ycor()>-400 and ball.xcor()<600:
                ball.goto(ball.xcor()+10,ball.ycor()-10)
            elif (ball.ycor()>-400):
                self.ball_left=True
                self.ball_right=False
            else:
                self.ball_down=False
                self.ball_up=True
        else:
            if ball.ycor()>-400 and ball.xcor()>-600:
                ball.goto(ball.xcor()-10,ball.ycor()-10)
            elif (ball.ycor()>-400):
                self.ball_left=False
                self.ball_right=True
            else :
                self.ball_down=False
                self.ball_up=True

    def ball_left_paddle_collision(self,ball,left_paddle):
        if (left_paddle.distance(ball.xcor(),ball.ycor())<50 and ball.xcor()<-540):
            self.ball_left=False
            self.ball_right=True
            self.timedelay=1.05*self.timedelay

    def ball_right_paddle_collision(self,ball,right_paddle):
       if (right_paddle.distance(ball.xcor(),ball.ycor())<50 and ball.xcor()>540):
           self.ball_left=True
           self.ball_right=False
           self.timedelay=1.05*self.timedelay
    

    def ball_wall_collision(self,ball):
        if (ball.distance(600,ball.ycor())<10):
            self.left_points+=1
            self.start(ball)
            return True
        if (ball.distance(-600,ball.ycor())<10):
            self.right_points+=1
            self.start(ball)
            return True
        return False
    
    def points(self):
        self.left_point.color("white")
        self.left_point.ht()
        self.left_point.up()
        self.left_point.bk(80)
        self.left_point.lt(90)
        self.left_point.fd(370)
        self.left_point.write(f"{self.left_points}" ,False, align="center", font=('Arial', 12, 'normal'))

        self.right_point.color("white")
        self.right_point.ht()
        self.right_point.up()
        self.right_point.fd(80)
        self.right_point.lt(90)
        self.right_point.fd(370)
        self.right_point.write(f"{self.right_points}" ,False, align="center", font=('Arial', 12, 'normal'))

    def update_points(self):
        self.left_point.clear()
        self.right_point.clear()
        self.left_point.write(f"{self.left_points}" , align="center", font=('Arial', 12, 'normal'))
        self.right_point.write(f"{self.right_points}" , align="center", font=('Arial', 12, 'normal'))





