from flask import Flask, render_template, jsonify, request
import json
import os
from game_logging import logger, log_powerups
from level_generator import generate_level

app = Flask(__name__)

# Ensure the levels directory exists
os.makedirs('levels', exist_ok=True)

@app.route('/')
def index():
    return render_template('level_editor.html')

@app.route('/api/levels', methods=['GET'])
def get_levels():
    levels = []
    for filename in os.listdir('levels'):
        if filename.startswith('level') and filename.endswith('.json'):
            try:
                with open(f'levels/{filename}', 'r') as f:
                    level_data = json.load(f)
                    level_number = int(filename[5:-5])  # Extract number from 'levelX.json'
                    levels.append({
                        'number': level_number,
                        'name': f'Level {level_number}',
                        'brick_count': sum(1 for row in level_data['bricks'] for brick in row if brick > 0)
                    })
            except:
                continue
    return jsonify(sorted(levels, key=lambda x: x['number']))

@app.route('/api/levels/<int:level_number>', methods=['GET'])
def get_level(level_number):
    try:
        with open(f'levels/level{level_number}.json', 'r') as f:
            level_data = json.load(f)
            # Log the allowed powerups for this level
            allowed_powerups = level_data.get('allowedPowerups', [])
            logger.info(f"Loading Level {level_number}")
            if allowed_powerups:
                log_powerups(allowed_powerups)
            else:
                logger.info("No powerups allowed in this level")
            
            # Log the powerups that will appear in this level
            powerups = level_data.get('powerups', [])
            if powerups:
                logger.info("Powerups that will appear in this level:")
                for powerup in powerups:
                    logger.info(f"- {powerup['type']} at position ({powerup['x']}, {powerup['y']})")
            else:
                logger.info("No powerups will appear in this level")
                
            return jsonify(level_data)
    except FileNotFoundError:
        logger.error(f"Level {level_number} not found")
        return jsonify({'error': 'Level not found'}), 404

@app.route('/api/levels/<int:level_number>', methods=['POST'])
def save_level(level_number):
    data = request.get_json()
    with open(f'levels/level{level_number}.json', 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Level {level_number} saved successfully")
    return jsonify({'success': True})

@app.route('/api/levels/<int:level_number>', methods=['DELETE'])
def delete_level(level_number):
    try:
        os.remove(f'levels/level{level_number}.json')
        logger.info(f"Level {level_number} deleted successfully")
        return jsonify({'success': True})
    except FileNotFoundError:
        logger.error(f"Failed to delete level {level_number}: Level not found")
        return jsonify({'error': 'Level not found'}), 404

@app.route('/api/generate-level', methods=['POST'])
def generate_level_route():
    data = request.get_json()
    pattern_type = data.get('pattern', 'random')
    
    try:
        # Generate the level using the level generator
        level_data = generate_level(pattern_type)
        logger.info(f"Generated level with pattern: {pattern_type}")
        return jsonify(level_data)
    except Exception as e:
        logger.error(f"Failed to generate level: {str(e)}")
        return jsonify({'error': 'Failed to generate level'}), 500

if __name__ == '__main__':
    logger.info("Starting DxBall level editor server")
    app.run(debug=True, port=5001) 