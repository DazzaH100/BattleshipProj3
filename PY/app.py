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