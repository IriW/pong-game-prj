# Pong Game Project

This project is a simple implementation of the classic Pong game using Python and the Turtle graphics library. It is part of the Udemy Course Challenge "100 Days of Code" and serves for learning purposes only as a Python learning project.

## Project Structure

- `main.py`: The main script that sets up the game screen, paddles, ball, and scoreboard. It contains the game loop and handles the game logic.
- `paddle.py`: Contains the `Paddle` class, which is responsible for creating and moving the paddles.
- `ball.py`: Contains the `Ball` class, which is responsible for creating and moving the ball, as well as handling collisions.
- `scoreboard.py`: Contains the `Scoreboard` class, which is responsible for keeping and displaying the score.
- `tests/`: Directory containing test files for the project.
  - `test_ball.py`: Contains unit tests for the `Ball` class.
  - `test_main.py`: Contains unit tests for the `Paddle` class.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the `main.py` script to start the game:
    ```sh
    python main.py
    ```

## How to Test

1. Ensure you have `pytest` installed:
    ```sh
    pip install pytest
    ```
2. Navigate to the project directory.
3. Run `pytest` to execute the tests:
    ```sh
    pytest
    ```

## Game Controls

- Use the `Up` and `Down` arrow keys to move the right paddle.
- Use the `W` and `S` keys to move the left paddle.

## Acknowledgements

This project is part of the Udemy Course Challenge "100 Days of Code" and serves for learning purposes only as a Python learning project.

Happy coding!