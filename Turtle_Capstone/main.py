import turtle
import game
import Level
import time

gameplay=game.Game()
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
score=Level.Levelboard()
score.initialize_board()
screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=gameplay.move_forward)

game_on=True
gameplay.start()
while game_on:
    screen.update()
    time.sleep(0.01)
    if gameplay.continue_game(screen):
        game_on=False
        # exit()
    if gameplay.john.ycor()>=280:
        score.update_board()
        gameplay.john.goto(0,-280)

screen.exitonclick()
