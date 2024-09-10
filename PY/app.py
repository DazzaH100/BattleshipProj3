from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the grid size and number of ships
GRID_SIZE = 5
NUM_SHIPS = 3

# Function to generate the grid and randomly place ships
def create_grid(size):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    ships = place_ships(size)
    return grid, ships

    # Function to place ships on the grid
def place_ships(size):
    ships = []
    while len(ships) < NUM_SHIPS:
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        if (x, y) not in ships:
            ships.append((x, y))
    return ships

    # Check if a guess is off the grid
def is_off_grid(guess, size):
    x, y = guess
    return x < 0 or x >= size or y < 0 or y >= size

    # Flask route to render the game page
@app.route('/')
def index():
    return render_template('index.html')

    # Route to start a new game
@app.route('/start_game', methods=['POST'])
def start_game():
    global GRID_SIZE
    grid_size = int(request.json.get('grid_size', GRID_SIZE))
    grid, ships = create_grid(grid_size)
    return jsonify({'grid': grid, 'ships': ships})

    # Route to handle a user guess
@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json.get('guess')
    grid_size = request.json.get('grid_size')
    ships = request.json.get('ships')

# Check if the guess is off-grid
    if is_off_grid(guess, grid_size):
        return jsonify({'error': 'Your guess is off the grid!'})

 # Check if the guess hits a ship
    if tuple(guess) in ships:
        return jsonify({'result': 'hit'})
    else:
        return jsonify({'result': 'miss'})

    
if __name__ == '__main__':
    app.run(debug=True)