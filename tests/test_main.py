import pytest
from unittest.mock import Mock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from paddle import Paddle

def test_paddle_movement():
    paddle = Paddle((0, 0))
    paddle.go_up = Mock()
    paddle.go_down = Mock()

    paddle.go_up()
    paddle.go_down()

    paddle.go_up.assert_called_once()
    paddle.go_down.assert_called_once()
