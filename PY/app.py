from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the grid size and number of ships
GRID_SIZE = 5
NUM_SHIPS = 3

#