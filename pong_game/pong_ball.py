from turtle import Turtle

class Ball(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("white")
      self.penup()
      self.x_move = 10
      self.y_move = 10
   
   def move_to(self):
      new_xcor = self.xcor() + self.x_move
      new_ycor = self.ycor() + self.y_move
      self.goto((new_xcor, new_ycor))

   def wall_bounce(self):
      self.y_move *= -1
   def paddle_bounce(self):
      self.x_move *= -1

   def reset_position(self):
      self.goto(0, 0)
      self.paddle_bounce()

