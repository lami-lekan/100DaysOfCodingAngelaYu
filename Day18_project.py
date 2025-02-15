from turtle import Turtle, Screen
import random

color = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black",
    "gray", "cyan", "magenta", "lime", "teal", "indigo", "violet", "gold", "silver", "beige"
]

# draws shapes
# count = 0
# angle = 360
# pace = 100
tim = Turtle()
tim.shape("turtle")
# tim.color("red")
# tim.pensize(2)


# for i in range(3, 11):
#     tim.pencolor(color[count])
#     for _ in range(i):
#         tim.right(angle / i)
#         tim.fd(pace)
#     count += 1


# random walk
turns = [0, 90, 180, 270]
pace = 30
tim.pensize(3)
tim.speed("fastest")

for step in range(1000):
    rand_turn = random.choice(turns)
    rand_color = random.choice(color)
    coin = random.randint(1,2)
    if coin == 2:
        tim.right(rand_turn)
    else:
        tim.left(rand_turn)
    tim.forward(pace)
    tim.pencolor(rand_color)


my_screen = Screen()
my_screen.screensize(2000,1500)
my_screen.exitonclick()
