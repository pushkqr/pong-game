from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random
from startscreen import StartScreen
import winsound

def quitGame():
    global is_over
    is_over = True
    ball.clear()
    r_paddle.clear()
    l_paddle.clear()
    scoreboard.gameOver()
    winsound.PlaySound(None, winsound.SND_PURGE)
    screen.bye()


def drawPartition(screen):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.color("black")
    turtle.shape("square")
    turtle.width(5)
    turtle.goto(0, 310)
    turtle.setheading(270)
    while turtle.ycor() > -280:
        turtle.pendown()
        turtle.fd(25)
        turtle.penup()
        turtle.fd(15)


is_over = False

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("cyan")
screen.title("Pong")
screen.tracer(0)
winsound.PlaySound("soundtrack.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

start = StartScreen()
start.launchGame(screen)

drawPartition(screen)
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.moveUp)
screen.onkeypress(key="Down", fun=r_paddle.moveDown)
screen.onkeypress(key="w", fun=l_paddle.moveUp)
screen.onkeypress(key="s", fun=l_paddle.moveDown)
screen.onkeypress(key="Escape", fun=quitGame)

while not is_over:
    screen.update()
    time.sleep(ball.speed)
    ball.move(l_paddle.pos(), r_paddle.pos())

    if ball.miss():
        if ball.xcor() > 0:
            ball.resetBall(random.choice([135, 225]))
            scoreboard.addPointLeft()
        elif ball.xcor() < 0:
            ball.resetBall(random.choice([45, 315]))
            scoreboard.addPointRight()

    if scoreboard.r_score >= 5 or scoreboard.l_score >= 5:
        ball.clear()
        r_paddle.clear()
        l_paddle.clear()
        screen.clear()
        scoreboard.gameOver()
        is_over = True
        winsound.PlaySound(None, winsound.SND_PURGE)
#screen.exitonclick()