from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player



game_screen = Screen()
game_screen.setup(600, 600)
game_is_on = True
game_screen.tracer(0)

player = Player()
score_board = Scoreboard()

game_screen.listen()
game_screen.onkey(player.move_up ,"Up")

car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    game_screen.update()
    car_manager.create_car()
    car_manager.moving_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()
        if player.is_player_on_finish_line():
            player.goto_start_line()
            car_manager.level_up()
            score_board.incr_level()
        
    

game_screen.exitonclick()