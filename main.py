from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

# TODO 1 : Create the screen
screen.setup(width=800, height=600)
screen.title("Pong-Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0, left_or_right="right")
l_paddle = Paddle(-350, 0, left_or_right="left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,   "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up,   "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5 : Detect collision with the wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 6 : Detect collision with paddle
    # distance measures from the centre of one object to another
    # so its not 20 which is width of both objects.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # TODO 7 : Detect when paddle misses
    if ball.xcor() > 380 :
        scoreboard.r_point()
        ball.reset_position()

    if ball.xcor() < -380 :
        scoreboard.l_point()
        ball.reset_position()
screen.exitonclick()

