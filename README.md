# DxBall Game

A Breakout/DxBall/Arkanoid-style game built with Python/Flask and HTML5 Canvas.

## Features

- Classic brick-breaking gameplay
- Multiple powerups with visual effects
- Level-based gameplay with JSON level files
- Score tracking and high scores system
- Lives system with game over conditions
- Built-in level editor
- Responsive web interface

### Powerups

- **Green**: Longer paddle (10 seconds)
- **Blue**: Faster paddle (10 seconds)
- **Yellow**: Multi-ball (up to 5 balls)
- **Purple**: Magnet paddle (10 seconds)
- **Red**: Extra Life

## Requirements

- Python 3.7+
- Flask
- python-dotenv

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dxball
```

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

- **Left Arrow**: Move paddle left
- **Right Arrow**: Move paddle right
- **Space**: Start game / Launch ball

## Project Structure

```
dxball/
├── app.py              # Flask web application
├── game.py             # Core game logic
├── game_logging.py     # Game logging utilities
├── level_editor.py     # Level editor functionality
├── level_generator.py  # Level generation utilities
├── levels/             # JSON level files
├── logs/               # Game logs (ignored in git)
├── scores/             # High scores data (ignored in git)
├── static/             # Static assets (fonts)
├── templates/          # HTML templates
└── requirements.txt    # Python dependencies
```

## Level System

### Playing Levels

The game includes 29 pre-built levels with varying difficulty and brick patterns. Levels are loaded sequentially, and players progress through them by clearing all bricks.

### Level Editor

Access the level editor at `http://localhost:5000/editor` to create custom levels:

- Click on the grid to toggle bricks
- Add powerups by clicking on the powerup buttons and then clicking on the grid
- Save your custom levels as JSON files

### Level File Format

Levels are stored in JSON format in the `levels/` directory. Each level file contains:

```json
{
    "bricks": [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ...
    ],
    "powerups": [
        {"type": "longer_paddle", "x": 200, "y": 100},
        {"type": "faster_paddle", "x": 400, "y": 150},
        ...
    ]
}
```

- **bricks**: A 16x12 grid where 1 = brick present, 0 = no brick
- **powerups**: Array of powerup objects with type and position

## Scoring System

- **Brick destroyed**: 10 points
- **Level completed**: 100 points bonus
- **Extra life**: Awarded every 1000 points
- **High scores**: Automatically saved and displayed

## Development

### Running Tests

```bash
python test_golden_ball.py
```

### Game Logging

Game events are logged to the `logs/` directory with timestamps. Logs include:
- Game start/end events
- Level progression
- Score changes
- Powerup activations

### Adding New Powerups

1. Define the powerup type in `game.py`
2. Add visual representation in the HTML template
3. Implement powerup logic in the game loop
4. Add powerup to the level editor interface

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by the classic DxBall and Breakout games
- Built with modern web technologies for cross-platform compatibility 