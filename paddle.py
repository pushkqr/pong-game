from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def moveUp(self):
        x = self.xcor()
        y = self.ycor()
        if self.ycor() < 230:
            self.setpos(x, y + 20)

    def moveDown(self):
        x = self.xcor()
        y = self.ycor()
        if self.ycor() > -230:
            self.setpos(x, y - 20)
