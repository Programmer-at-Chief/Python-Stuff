# import turtle
from turtle import Turtle

class Score(Turtle):
    current_score=0
    try:
        with open("high_score.txt","r") as file:
            high_score=int(file.read().rstrip('\n'))
    except:
        high_score=0
    # self.hide()
    def __init__(self):
        super().__init__()
    def display_score(self):
        self.goto((0,260))
        self.write(f"Score : {self.current_score} High Score : {self.high_score}", False, align="center", font=('Arial', 12, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ", False, align="center", font=('Arial', 14, 'bold'))

        
    def increase_score(self):
        self.clear()
        self.current_score+=1
        self.display_score()

    def reset(self):
        self.clear()
        self.current_score=0
        self.display_score()
