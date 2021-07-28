from turtle import Turtle
import random
import math
import numpy
SPEED = 10
INITIAL_ANGLE = random.randint(-45, 45)*math.pi/180
INITIAL_DIRECTION = random.choice([-1, 1])


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(-30, 0)
        self.speed = (INITIAL_DIRECTION*SPEED*math.cos(INITIAL_ANGLE), SPEED*math.sin(INITIAL_ANGLE))
        print(self.speed)

    def move(self):
        self.setpos(numpy.add(self.pos(), self.speed))