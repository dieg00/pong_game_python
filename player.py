from turtle import Turtle
Y_POSITIONS = [20, 0, -20]
X_LEFT_POSITION = -390
X_RIGHT_POSITION = 390
STEP = 10

class Player:
    def __init__(self):
        self.player = []
        for n in range(3):
            block = Turtle("square")
            block.penup()
            block.color("white")
            block.setpos(0, Y_POSITIONS[n])
            self.player.append(block)

    def left(self):
        for block in self.player:
            block.setx(X_LEFT_POSITION)

    def right(self):
        for block in self.player:
            block.setx(X_RIGHT_POSITION)

    def down(self):
        for block in self.player:
            block.sety(block.ycor()-STEP)

    def up(self):
        for block in self.player:
            block.sety(block.ycor() + STEP)
