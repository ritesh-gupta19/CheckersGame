# Checkers Game

Welcome to the Checkers game project! This is a Python-based implementation using the Pygame library, featuring an AI opponent powered by the Minimax algorithm.

## Features

- **Two-player mode:** Play against an AI opponent.
- **AI using Minimax:** The AI utilizes the Minimax algorithm with alpha-beta pruning for optimal moves.
- **Graphical Interface:** Built using Pygame for an interactive gaming experience.
- **User Interaction:** Click-based movement for intuitive gameplay.

## Requirements

- Python 3.x
- Pygame

## Installation

To run this project on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/checkers-game.git
    cd checkers-game
    ```
2. **Install the required dependencies:**
    ```bash
    pip install pygame
    ```

## How to Play

1. **Start the game:** Run the `main.py` script.
    ```bash
    python main.py
    ```
2. **Make a move:** Click on a piece to select it, and then click on the target square to move.
3. **Winning:** The game will declare the winner when one player has no legal moves left.

## Project Structure

- `main.py`: The main script to run the game.
- `checkers/`: Directory containing the core game logic.
    - `constants.py`: Game constants such as colors and board dimensions.
    - `game.py`: The Game class managing game state, updating, and drawing.
- `minimax/`: Directory with the AI algorithm.
    - `algorithm.py`: Implementation of the Minimax algorithm.

