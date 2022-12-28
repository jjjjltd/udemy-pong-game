from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.score = 0

    def goup(self):
        self.setheading(UP)
        self.forward(20)

    def godown(self):
        self.setheading(DOWN)
        self.forward(20)
    
    def add_score():
        self += 1
    
