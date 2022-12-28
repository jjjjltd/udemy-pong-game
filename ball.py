from turtle import Turtle
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(0.1)
        self.direction = "F"
        self.start_pos()
    
    def start_pos(self):
        startx = random.randint(-350, 350)
        starty = random.randint(-350, 350)
        # self.goto(startx, starty)
        self.goto(0,0)
        
    def bounce(self, heading):
        self.setheading(360-heading)
        # self.backward(100)
        # self.direction = "B"

