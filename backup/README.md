# DxBall Game

A Breakout/DxBall/Arkanoid-style game built with Python/Flask and HTML5 Canvas.

## Features

- Classic brick-breaking gameplay
- Powerups:
  - Longer paddle
  - Faster paddle
  - Multi-ball (up to 5 balls)
  - Magnet paddle
  - Extra Life
- Level-based gameplay with JSON level files
- Score tracking and lives system

## Requirements

- Python 3.7+
- Flask
- python-dotenv

## Installation

1. Clone the repository
2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Running the Game

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Controls

- Left Arrow: Move paddle left
- Right Arrow: Move paddle right

## Level Files

Levels are stored in JSON format in the `levels` directory. Each level file contains:
- A 16x12 grid of bricks (1 = brick present, 0 = no brick)
- Powerup spawn locations

Example level structure:
```json
{
    "bricks": [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ...
    ],
    "powerups": [
        {"type": "longer_paddle", "x": 200, "y": 100},
        ...
    ]
}
```

## Powerups

- Green: Longer paddle (10 seconds)
- Blue: Faster paddle (10 seconds)
- Yellow: Multi-ball (up to 5 balls)
- Purple: Magnet paddle (10 seconds) 