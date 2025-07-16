import random
import json

# Game constants
BRICK_COLUMNS = 16
BRICK_ROWS = 12

# Brick types
EMPTY = 0
REGULAR = 1
DOUBLE = 2
MAGNETIC = 3
TELEPORT = 4
METAL = 5
EXPLOSIVE = 6

def generate_empty_level():
    """Generate an empty level with no bricks."""
    return {
        'bricks': [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)],
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_simple_pattern():
    """Generate a simple pattern level."""
    bricks = [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)]
    
    # Create alternating rows of regular and double bricks
    for row in range(4):
        for col in range(BRICK_COLUMNS):
            if row % 2 == 0:
                bricks[row][col] = REGULAR
            else:
                bricks[row][col] = DOUBLE if col % 2 == 0 else REGULAR
    
    return {
        'bricks': bricks,
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_pyramid_pattern():
    """Generate a pyramid pattern level."""
    bricks = [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)]
    
    center = BRICK_COLUMNS // 2
    for row in range(6):
        width = row + 1
        start_col = center - width // 2
        end_col = center + width // 2
        
        for col in range(start_col, end_col + 1):
            if 0 <= col < BRICK_COLUMNS:
                if row < 2:
                    bricks[row][col] = REGULAR
                elif row < 4:
                    bricks[row][col] = DOUBLE
                else:
                    bricks[row][col] = MAGNETIC
    
    return {
        'bricks': bricks,
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_checkerboard_pattern():
    """Generate a checkerboard pattern level."""
    bricks = [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)]
    
    for row in range(6):
        for col in range(BRICK_COLUMNS):
            if (row + col) % 2 == 0:
                bricks[row][col] = REGULAR
            else:
                if random.random() < 0.7:  # 70% chance of placing a brick
                    bricks[row][col] = DOUBLE
    
    return {
        'bricks': bricks,
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_random_pattern():
    """Generate a random pattern level."""
    bricks = [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)]
    
    # Fill first 6 rows with random bricks
    brick_types = [REGULAR, DOUBLE, MAGNETIC, TELEPORT]
    
    for row in range(6):
        for col in range(BRICK_COLUMNS):
            if random.random() < 0.6:  # 60% chance of placing a brick
                bricks[row][col] = random.choice(brick_types)
    
    # Add some metal bricks scattered around
    for _ in range(random.randint(3, 8)):
        row = random.randint(0, 5)
        col = random.randint(0, BRICK_COLUMNS - 1)
        bricks[row][col] = METAL
    
    # Add a few explosive bricks
    for _ in range(random.randint(1, 3)):
        row = random.randint(0, 5)
        col = random.randint(0, BRICK_COLUMNS - 1)
        bricks[row][col] = EXPLOSIVE
    
    return {
        'bricks': bricks,
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_fortress_pattern():
    """Generate a fortress/castle pattern level."""
    bricks = [[EMPTY for _ in range(BRICK_COLUMNS)] for _ in range(BRICK_ROWS)]
    
    # Outer walls with metal bricks
    for row in range(4):
        for col in range(BRICK_COLUMNS):
            if col < 2 or col >= BRICK_COLUMNS - 2:  # Side walls
                bricks[row][col] = METAL
            elif row == 0:  # Top wall
                bricks[row][col] = METAL
    
    # Inner area with regular and double bricks
    for row in range(1, 3):
        for col in range(3, BRICK_COLUMNS - 3):
            if random.random() < 0.8:
                bricks[row][col] = REGULAR if random.random() < 0.7 else DOUBLE
    
    # Add some towers
    for col in [1, BRICK_COLUMNS - 2]:
        for row in range(5):
            if row < 4 or (row == 4 and col % 4 == 1):
                bricks[row][col] = METAL
    
    return {
        'bricks': bricks,
        'powerups': [],
        'allowedPowerups': ['longer_paddle', 'faster_paddle', 'multi_ball', 'magnet', 'extra_life']
    }

def generate_level(pattern_type='random'):
    """Generate a level based on the specified pattern type."""
    patterns = {
        'empty': generate_empty_level,
        'simple': generate_simple_pattern,
        'pyramid': generate_pyramid_pattern,
        'checkerboard': generate_checkerboard_pattern,
        'random': generate_random_pattern,
        'fortress': generate_fortress_pattern
    }
    
    generator = patterns.get(pattern_type, generate_random_pattern)
    return generator()

def save_generated_level(level_data, level_number):
    """Save the generated level to a file."""
    filename = f'levels/level{level_number}.json'
    with open(filename, 'w') as f:
        json.dump(level_data, f, indent=4)
    return filename

if __name__ == '__main__':
    # Example usage
    import sys
    
    pattern_type = sys.argv[1] if len(sys.argv) > 1 else 'random'
    level_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    level_data = generate_level(pattern_type)
    filename = save_generated_level(level_data, level_number)
    print(f"Generated {pattern_type} level saved to {filename}") 