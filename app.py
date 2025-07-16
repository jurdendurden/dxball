from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Game constants
GAME_WIDTH = 800
GAME_HEIGHT = 600
BRICK_COLUMNS = 16
BRICK_ROWS = 12
BRICK_WIDTH = GAME_WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 30
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 12
BALL_RADIUS = 10

# Ensure the scores directory exists
os.makedirs('scores', exist_ok=True)
SCORES_FILE = 'scores/high_scores.json'

def load_level(level_number):
    try:
        with open(f'levels/level{level_number}.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/level/<int:level_number>')
def get_level(level_number):
    level_data = load_level(level_number)
    if level_data:
        return jsonify(level_data)
    return jsonify({'error': 'Level not found'}), 404

@app.route('/api/scores', methods=['GET'])
def get_scores():
    scores = load_scores()
    return jsonify(scores)

@app.route('/api/scores', methods=['POST'])
def add_score():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    
    if not name or not isinstance(score, int):
        return jsonify({'error': 'Invalid data'}), 400
    
    scores = load_scores()
    scores.append({'name': name, 'score': score})
    scores.sort(key=lambda x: x['score'], reverse=True)
    scores = scores[:10]  # Keep only top 10
    
    save_scores(scores)
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True) 