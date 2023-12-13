# Pong Game

A classic two-player Pong game implemented in Python using the Turtle graphics library.

## Description

This Pong game is a simple implementation of the classic Pong arcade game. It features two paddles, a ball, and a partition in the middle. The objective is to bounce the ball back and forth between the paddles without letting it pass your own paddle.

## Features

- Two-player Pong game.
- Start screen with game instructions.
- Score tracking and game-over screen.
- Background sound effects.

## Controls

- Player 1 (Left Paddle):
  - Move Up: W key
  - Move Down: S key

- Player 2 (Right Paddle):
  - Move Up: Arrow Up key
  - Move Down: Arrow Down key

- Quit Game: Escape key

## Gameplay

- The game starts with a welcome screen displaying the game title and instructions.
- Players use their respective controls to move their paddles up and down.
- The ball moves between the paddles, and each time it passes a paddle, the opposing player scores a point.
- The game ends when one player reaches a score of 5 points.
- A game-over screen is displayed, and the game can be restarted.

## Compilation and Usage

**Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/pong-game.git
   cd pong-game
   python main.py
