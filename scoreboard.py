from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def addPointLeft(self):
        self.l_score += 1
        self.update()

    def addPointRight(self):
        self.r_score += 1
        self.update()

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 60, "bold"))
        self.goto(0, -100)
        self.write(f"{'Player 1 Wins!' if self.l_score > self.r_score else 'Player 2 Wins!'}", align="center", font=("Arial", 40, "italic"))
        time.sleep(2)
