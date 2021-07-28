from turtle import Screen, onkeypress
from table import Table
from player import Player
from ball import Ball
import time

#Creates basic elements
screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=900)
screen.tracer(0)

table = Table()
p1 = Player()
p1.left()
p2 = Player()
p2.right()
onkeypress(fun=p1.up, key="w")
onkeypress(fun=p2.up, key="Up")
onkeypress(fun=p1.down, key="s")
onkeypress(fun=p2.down, key="Down")
screen.listen()
ball = Ball()

game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(0.01)




screen.exitonclick()