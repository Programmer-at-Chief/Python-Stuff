import turtle
import random as rand
import time

color_code=["white","blue","pink","green","yellow","red"]

class Game:
    queue=[]
    john=turtle.Turtle()
    def __init__(self):
        self.john.shape("turtle")
        self.john.color("white")
        self.john.up()
        self.john.lt(90)
        self.john.goto(0,-280)
    def start(self):
        for i in range(20):
            tur=turtle.Turtle()
            tur.shape("square")
            tur.rt(180)
            tur.color(rand.choice(color_code))
            tur.up()
            tur.goto(rand.randrange(-400,400),rand.randrange(-250,250))
            self.queue.append(tur)
    def continue_game(self,screen):
        num=rand.randrange(3)
        for i in range(num):
            tur=turtle.Turtle()
            tur.shape("square")
            tur.rt(180)
            tur.color(rand.choice(color_code))
            tur.up()
            tur.goto(400,rand.randrange(-250,250))
            self.queue.append(tur)
        for i in range(0,len(self.queue)-1,1):
            if (self.john.distance(self.queue[i])<30):
                self.john.write("Game Over", False, align="center", font=('Arial', 14, 'normal'))
                return True
            self.queue[i].fd(20)
            if self.queue[i].xcor()<=-380 :
                # del self.queue[i]
                # i-=1
                self.queue[i].ht()
                # self.queue.remove(i)
                # screen.remove(i)
            # return False 

    def move_forward(self):
        self.john.fd(20)



