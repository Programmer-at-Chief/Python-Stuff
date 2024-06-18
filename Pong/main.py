import turtle
import setup
import logic

screen=turtle.Screen()
# screen.setup(width=800,height=600)
screen.setup(width=1200,height=800)
screen.bgcolor("black")

game=setup.Pong()
game.mid_line()

game.create_paddle_left()
game.create_paddle_right()
game.ball()

mind=logic.Logic()

screen.listen()
screen.onkey(key="w",fun=game.left_paddle_up)
screen.onkey(key="s",fun=game.left_paddle_down)
screen.onkey(key="Up",fun=game.right_paddle_up)
screen.onkey(key="Down",fun=game.right_paddle_down)
# screen.onkey(key="q",fun=exit())
# screen.onkey(key="Space",game_on=True)
mind.points()

game_on = True
while game_on:
    screen.update()
    mind.start(game.play_ball)
    if mind.ball_wall_collision(game.play_ball):
        mind.update_points()

    # mind.update_points()


    mind.ball_left_paddle_collision(game.play_ball,game.paddle_left) 
    mind.ball_right_paddle_collision(game.play_ball,game.paddle_right)
        
    if (mind.right_points==10 or mind.left_points==10):
        game_on= False

if (mind.right_points==10):
    print("Player on the right , wins !!.")
else:
    print("Player on the left , wins !!.")



screen.exitonclick()
