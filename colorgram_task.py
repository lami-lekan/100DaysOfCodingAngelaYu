from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
# import colorgram
# rgb_color = []
# colors = colorgram.extract("hirst_paint.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)


rgb_tuple = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

for r in range(10):
    for c in range(10):
        tim.dot(20, random.choice(rgb_tuple))
        tim.up()
        tim.fd(50)
    tim.up()

screen = Screen()
screen.exitonclick()