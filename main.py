from centre_line import Centre_Line
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

WIDTH = 800
HEIGHT = 600
FORWARD = 20

def rightup(paddle):
    paddle.setheading(90)
    paddle.forward(10)

def rightdown(paddle):
    paddle.setheading(270)
    paddle.forward(10)

def leftup(paddle):
    paddle.setheading(90)
    paddle.forward(10)

def leftdown(paddle):
    paddle.setheading(270)
    paddle.forward(10)

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Eleanor Angry Tennis Game")
t = Centre_Line()


# Draw centre line
t.goto(0,-0.5*HEIGHT)
Steps = (screen.window_height() // FORWARD + 1)
for _ in range(Steps):
    t.dot()
    t.forward(FORWARD)

right_paddle = Paddle()
right_paddle.goto((WIDTH / 2) - 30, 0)
left_paddle = Paddle()
left_paddle.goto(-1 * ((WIDTH / 2) - 30), 0)
billy = Ball()
screen.tracer(0)
screen.listen()
screen.onkey(right_paddle.goup, "Up")
screen.onkey(right_paddle.godown, "Down")
screen.onkey(left_paddle.goup, "s")
screen.onkey(left_paddle.godown, "x")

def print_heading(heading):
    print(f"Should be heading away {heading}")

if billy.ycor() < 0:
    billy.setheading(random.randint(91,270))
else:
    billy.setheading(random.randint(271, 350))

billy.setheading(80)

boundary = ((screen.window_height() // 2)-10)
wall_boundary = ((screen.window_width() // 2) - 80)   
scoreboard = Scoreboard()
scoreboard.increase_score()
scoreboard.update_scoreboard()

paddle_met = False
play_on = True
while play_on:
    # time.sleep(0.5)
    screen.update()    
    billy.setheading(billy.heading())
    billy.forward(1)

    if billy.ycor() >= boundary or billy.ycor() <= -1 * boundary:
        billy.bounce(billy.heading())

    if paddle_met == False:

        if (billy.distance(right_paddle) < 50 and billy.xcor() > wall_boundary):  
            billy.bounce(billy.heading())
            paddle_met = True
        
        if (billy.distance(left_paddle) < 50 and billy.ycor() < -1 * wall_boundary):
            billy.bounce(billy.heading())
            paddle_met = True
    
    else:

        if billy.distance(left_paddle) > 50 and billy.distance(right_paddle) > 50:
            paddle_met = False
    
    
screen.exitonclick()