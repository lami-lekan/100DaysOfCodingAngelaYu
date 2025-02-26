from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 14, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.write_score()
        self.hideturtle()
        
    def write_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        
        
    def score_update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)