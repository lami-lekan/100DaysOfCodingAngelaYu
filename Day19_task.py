from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forwards():
    tim.fd(20)
def move_backwards():
    tim.back(20)
def counterclockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_screen():
    tim.reset()

my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(counterclockwise, "a")
my_screen.onkey(clockwise, "d")
my_screen.onkey(clear_screen, "c")
my_screen.exitonclick()