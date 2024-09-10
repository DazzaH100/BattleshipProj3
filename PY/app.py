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