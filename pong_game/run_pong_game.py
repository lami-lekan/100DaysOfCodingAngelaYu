from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from scoreboard import Scoreboard
import time

#To set up game screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.tracer(0)

start_pong = True

l_paddle = Paddle()
r_paddle = Paddle()
pong_ball = Ball()
score = Scoreboard()

l_paddle.move_to((-385, 0))
r_paddle.move_to((379, 0))

#To get commands from keyboard
game_screen.listen()
game_screen.onkey(r_paddle.go_up, "Up")
game_screen.onkey(r_paddle.go_down, "Down")
game_screen.onkey(l_paddle.go_up, "w")
game_screen.onkey(l_paddle.go_down, "s")

while start_pong:
    game_screen.update()
    time.sleep(0.1)
    pong_ball.move_to()

    # To detect collision with wall
    if pong_ball.ycor() == 280 or pong_ball.ycor() == -280:
        pong_ball.wall_bounce()

    #To detect collision with paddle
    if r_paddle.distance(pong_ball) < 30 and pong_ball.xcor() < 380 or l_paddle.distance(pong_ball) < 30 and pong_ball.xcor() < -350 :
        pong_ball.paddle_bounce()

    #To detect when ball goes out of play
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()

game_screen.exitonclick()