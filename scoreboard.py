from turtle import Turtle
SEPARATION = 230

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.sety(280)
        self.color("white")
        self.score = 0

    def write_score(self):
        self.write(arg=f"{self.score}", align="center", font =("Arial", 50, "bold"))

    def set_left(self):
        self.setx(-SEPARATION)
        self.write_score()

    def set_right(self):
        self.setx(SEPARATION)
        self.write_score()

    def add_point(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_card(self):
        self.setpos(0, -72)
        self.write(arg="P O I N T !", align="center", font=("Arial", 90, "bold"))
