from turtle import Turtle, Screen
from snake import Snake
import time

is_game_on = True
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")

snake = Snake()

# game_screen.listen()
# game_screen.onkey(snake.turn("up"), "Up")
# game_screen.onkey(snake.turn("down"), "Down")
# game_screen.onkey(snake.turn("right"), "Right")
# game_screen.onkey(snake.turn("left"), "Left")

while is_game_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()
    

game_screen.exitonclick()