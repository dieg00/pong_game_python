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


def new_game():
    ball.new_game()
    p1.reset()
    p2.reset()
    time.sleep(3)


game_on = True

while game_on:
    screen.update()
    ball.move()
    ball.check_bounce()
    for n in range(len(p1.player)):
        if ball.distance(p1.player[n]) < 18 or ball.distance(p2.player[n]) < 18:
            ball.horizontal_bounce()
            for _ in range(10):
                ball.move()
                screen.update()
                time.sleep(0.016666667)
            break
    if ball.escaped():
        new_game()

    time.sleep(0.016666667)




screen.exitonclick()