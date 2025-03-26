from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 14, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.goto(0,270)
        self.write_score()
        self.hideturtle()
        
    def write_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)
        
        
    def score_update(self):
        self.clear()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as high_score:
                high_score.write(str(self.score)) 
        self.score = 0
        self.score_update()