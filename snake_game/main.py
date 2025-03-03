from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

is_game_on = True
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.right, "Right")
game_screen.onkey(snake.left, "Left")

while is_game_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()

    # detect colision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()
    
    # detect colision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
    

game_screen.exitonclick()