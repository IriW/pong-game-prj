import pytest
from turtle import Screen
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ball import Ball

def test_ball_initialization():
    ball = Ball()
    assert ball.x_move == 10
    assert ball.y_move == 10
@pytest.fixture
def ball():
    screen = Screen()
    screen.setup(width=800, height=600)
    return Ball()

def test_ball_initial_position(ball):
    assert ball.xcor() == 0
    assert ball.ycor() == 0

def test_ball_move(ball):
    initial_x = ball.xcor()
    initial_y = ball.ycor()
    ball.move()
    assert ball.xcor() == initial_x + ball.x_move
    assert ball.ycor() == initial_y + ball.y_move

def test_ball_bounce_y(ball):
    initial_y_move = ball.y_move
    ball.bounce_y()
    assert ball.y_move == -initial_y_move

def test_ball_bounce_x(ball):
    initial_x_move = ball.x_move
    initial_speed = ball.move_speed
    ball.bounce_x()
    assert ball.x_move == -initial_x_move
    assert ball.move_speed == initial_speed * 0.9
