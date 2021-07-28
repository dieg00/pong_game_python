from turtle import Turtle
POSITIONS = [-330, -310, -250, -230, -170, -150, -90, -70, -10, 10, 70, 90, 150, 170, 230, 250, 310, 330]

class Table():
    def __init__(self):
        for n in range(len(POSITIONS)):
            block = Turtle("square")
            block.penup()
            block.color("white")
            block.setpos(0, POSITIONS[n])

