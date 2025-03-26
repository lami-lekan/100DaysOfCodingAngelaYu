from turtle import Turtle
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def incr_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", font=FONT)