# TO DO:
# Create the screen
# Create and move the paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_point()  # Reward for bouncing off the right paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_point()  # Reward for bouncing off the left paddle

    # Detect when R paddle misses the ball, if yes - reset ball position
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when L paddle misses the ball, if yes - reset ball position
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()