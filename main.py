from turtle import Screen, onkeypress, onkey
from table import Table
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

#Creates basic elements
screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=900)
screen.tracer(0)
screen.title("Pong")
table = Table()
p1 = Player()
p1.left()
p2 = Player()
p2.right()
s1 = Scoreboard()
s1.set_left()
s2 = Scoreboard()
s2.set_right()
card = Scoreboard()
game_on = True
stopped = False
onkeypress(fun=p1.up, key="w")
onkeypress(fun=p2.up, key="Up")
onkeypress(fun=p1.down, key="s")
onkeypress(fun=p2.down, key="Down")


def finish_game():
    global game_on
    game_on = False
    print("Hey")


def pause_game():
    global stopped
    stopped = True
    # if stopped:
    #     stopped = False
    # else:
    #     stopped = True


onkeypress(fun=finish_game, key="Escape")
onkey(fun=pause_game, key="space")

screen.listen()
ball = Ball()


def new_game():
    card.write_card()
    screen.update()
    time.sleep(3)
    card.clear()
    ball.new_game()
    p1.reset()
    p2.reset()


while game_on:
    onkey(fun=pause_game, key="space")
    screen.listen()
    print(stopped)
    screen.update()
    ball.move()
    ball.check_bounce()
    for n in range(len(p1.player)):
        if ball.distance(p1.player[n]) < 18 or ball.distance(p2.player[n]) < 18:
            ball.horizontal_bounce()
            ball.increase_speed(1.1)
            for _ in range(10):
                ball.move()
                ball.check_bounce()
                screen.update()
                time.sleep(0.016666667)
            break
    if ball.escaped():
        if ball.xcor() > 0:
            s1.add_point()
        else:
            s2.add_point()
        new_game()

    time.sleep(0.016666667)
    while stopped:
        # onkey(fun=pause_game, key="space")
        # screen.listen()
        # time.sleep(0.5)
        screen.textinput(title="Continue?", prompt="Press Enter to continue playing.")
        stopped = False
