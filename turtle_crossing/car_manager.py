from turtle import Turtle
import random
COLORS = ["red", "orange", "black", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:    
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(.9, 1.8)
            new_car.resizemode("user")
            new_car.color(random.choice(COLORS))
            new_car.goto(330, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def moving_cars(self):
        for car in self.all_cars:
            car.back(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT