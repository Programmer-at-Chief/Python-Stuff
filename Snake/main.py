import turtle
import random
import time
import snake
import scoreboard 

screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Drake Origins")
screen.tracer(0)

snoke=snake.Snake()
snoke.create_snake()

scores=scoreboard.Score()
scores.color("white")
scores.hideturtle()
scores.up()
scores.display_score()

snoke.food()
consumed=False;
screen.listen()
game_on=True
count=0;
while game_on:
    screen.update()
    time.sleep(0.1)
    snoke.move()
    screen.onkey(key="Left",fun=snoke.go_left)
    screen.onkey(key="Right",fun=snoke.go_right)
    screen.onkey(key="Down",fun=snoke.go_down)
    screen.onkey(key="Up",fun=snoke.go_up)
    screen.onkey(key="q",fun=scores.game_over)
    if (snoke.head.distance(snoke.food_tur.pos())<=15):
        snoke.eaten()
        consumed=True
        scores.increase_score()
    if (consumed):
        snoke.food()
        consumed=False;
    if (snoke.segment[0].xcor()>300 or snoke.segment[0].xcor()< -300 or snoke.segment[0].ycor()>300 or snoke.segment[0].ycor()< -300):
        if (scores.current_score>scores.high_score):
            scores.high_score=scores.current_score
        with open("high_score.txt","w") as file:
            file.write(f"{scores.high_score}")
        scores.reset()
        snoke.reset()
        snoke.move()
        continue
    # elif ():
    for parts in range(1,snoke.length):
        if (snoke.head.distance(snoke.segment[parts])<15):
            if (scores.current_score>scores.high_score):
                scores.high_score=scores.current_score
            with open("high_score.txt","w") as file:
                file.write(f"{scores.high_score}")
            scores.reset()
            snoke.reset()
            snoke.move()
            break
    # count+=1



screen.exitonclick()
