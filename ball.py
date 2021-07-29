from turtle import Turtle
import random
import math
import numpy

SPEED = 10



class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.INITIAL_ANGLE = random.randint(-45, 45) * math.pi / 180
        self.INITIAL_DIRECTION = random.choice([-1, 1])
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)
        self.speed = (self.INITIAL_DIRECTION*SPEED*math.cos(self.INITIAL_ANGLE), SPEED*math.sin(self.INITIAL_ANGLE))


    def move(self):
        self.setpos(numpy.add(self.pos(), self.speed))

    def check_bounce(self):
        if abs(self.ycor()) > 330:
            self.vertical_bounce()
        # elif abs(self.xcor()) > 400:
        #     self.horizontal_bounce()

    def vertical_bounce(self):
        self.speed = (self.speed[0], 0 - self.speed[1])

    def horizontal_bounce(self):
        self.speed = (0 - self.speed[0], self.speed[1])

    def escaped(self):
        if abs(self.xcor()) > 500:
            return True
        else:
            return False

    def increase_speed(self, step):
        self.speed = tuple([x * step for x in self.speed])

    def new_game(self):
        self.INITIAL_ANGLE = random.randint(-45, 45) * math.pi / 180
        self.INITIAL_DIRECTION = random.choice([-1, 1])
        self.setpos(0, 0)
        self.speed = (self.INITIAL_DIRECTION*SPEED*math.cos(self.INITIAL_ANGLE), SPEED*math.sin(self.INITIAL_ANGLE))
