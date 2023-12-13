from turtle import Turtle
import random

start_dir = [45, 135, 315, 225]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.04
        self.color("black")
        self.shape("circle")
        self.penup()
        self.setheading(random.choice(start_dir))

    def move(self, paddle1_pos, paddle2_pos):
        x = self.xcor()
        y = self.ycor()

        if y >= 280 and self.heading() == 45:
            self.setheading(315)
        elif y >= 280 and self.heading() == 135:
            self.setheading(225)
        elif y <= -280 and self.heading() == 225:
            self.setheading(135)
        elif y <= -280 and self.heading() == 315:
            self.setheading(45)
        elif abs(paddle2_pos[0] - x) <= 20 and abs(paddle2_pos[1] - y) <= 50:
            if self.heading() == 315:
                self.setheading(225)
                self.increaseSpeed()
            elif self.heading() == 45:
                self.setheading(135)
                self.increaseSpeed()
        elif abs(paddle1_pos[0] - x) <= 20 and abs(paddle1_pos[1] - y) <= 50:
            if self.heading() == 135:
                self.setheading(45)
                self.increaseSpeed()
            elif self.heading() == 225:
                self.setheading(315)
                self.increaseSpeed()
        self.fd(10)

    def miss(self):
        """Returns 'true' if out of bounds , 'false' o.w"""
        x = self.xcor()
        y = self.ycor()

        if 280 > y > -280 and x > 380:
            return True
        elif 280 > y > -280 and x < -380:
            return True
        else:
            return False

    def resetBall(self, angle):
        self.setpos(0, 0)
        self.setheading(angle)
        self.speed = 0.03

    def increaseSpeed(self):
        if self.speed > 0.015:
            self.speed -= 0.0025
