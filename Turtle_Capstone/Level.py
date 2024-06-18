import turtle

class Levelboard(turtle.Turtle):
    current_score=0
    def __init__(self):
        super().__init__()
    def initialize_board(self):
        self.ht()
        self.color("white")
        self.up()
        self.goto(-330,260)
        self.write(f"Score : {self.current_score}", False, align="center", font=('Arial', 12, 'normal'))
    def update_board(self):
        self.clear()
        self.current_score+=1
        self.write(f"Score : {self.current_score}", False, align="center", font=('Arial', 12, 'normal'))



