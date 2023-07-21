from turtle import Turtle
import time

class StartScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()

    def launchGame(self):
        for i in range(3, 0, -1):
            self.color("black")
            self.goto(0, 50)
            self.write("🏓 PONG 🏓", align="center", font=("Roman", 120, "bold"))
            self.goto(0, -50)
            self.write(f"Game starts in {i}...", align="center", font=("Roman", 30, "normal"))
            self.goto(0, -150)
            #self.color("skyblue")
            self.write("|Controls|", align="center", font=("Roman", 30, "bold"))
            self.goto(0, -200)
            #self.color("red")
            self.write("Player 1: up - W, down - S", align="center", font=("Courier", 15, "bold"))
            self.goto(0, -250)
            #self.color("red")
            self.write("Player 2:up - Arrow Up, down - Arrow Down", align="center", font=("Courier", 15, "bold"))
            time.sleep(1.5)
            self.clear()

        self.goto(0, 0)
        self.write("First to 5 wins!", align="center", font=("Roman", 40, "italic"))
        time.sleep(1.5)
        self.clear()

