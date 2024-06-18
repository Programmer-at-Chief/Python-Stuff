# while inheriting classes super() keyword can be used to associate the parent class
import turtle
import random

STARTING_POSN={(0,0),(20,0),(40,0)}
DISTANCE=20

class Snake:
    food_tur=turtle.Turtle()
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.length=len(self.segment)
        self.head=self.segment[0]
    def create_snake(self):
        for posn in STARTING_POSN:
            tur=turtle.Turtle(shape="square")
            tur.color("white")
            tur.up()
            tur.goto(posn)
            self.segment.append(tur)
        self.head=self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            num_x=self.segment[seg_num-1].xcor()
            num_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(num_x,num_y)
        self.segment[0].fd(DISTANCE)
    def go_up(self):
        if (int(self.segment[0].heading())!=270):
            self.segment[0].seth(90)
    def go_right(self):
        if (int(self.segment[0].heading())!=180):
            self.segment[0].seth(0)
    def go_left(self):
        if (int(self.segment[0].heading())!=0):
            self.segment[0].seth(180)
    def go_down(self):
        if (int(self.segment[0].heading())!=90):
            self.segment[0].seth(270)
    def food(self):
        self.food_tur.goto(random.randrange(-280,280),random.randrange(-280,280))
        self.food_tur.dot(20,"blue")
    def eaten(self):
        self.food_tur.clear()
        tur=turtle.Turtle(shape="square")
        tur.color("white")
        tur.up()
        tur.goto(self.segment[len(self.segment)-1].xcor(),self.segment[len(self.segment)-1].ycor())
        self.segment.append(tur)
        self.segment[0].speed(self.segment[0].speed()+1)
        self.length+=1
    def checkdeath(self):
        length=len(self.segment)
        for i in range(0,length-3):
            if (self.segment[length-1].xcor() == self.segment[i].xcor() and self.segment[length-1].ycor() == self.segment[i].ycor()):
                return False
        return True
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.length=len(self.segment)
        self.create_snake()

