import numpy as np
from numpy.random import shuffle

class genAlgo:
    def __init__(self, h, w):
        # Validate maze dimensions
        if h <= 0 or w <= 0:
            raise ValueError(f"Maze dimensions must be positive integers, got h={h}, w={w}")
        # Initialize maze dimensions
        self.h = int(h)
        self.w = int(w)
        # Calculate grid dimensions with walls included
        self.H = (2*self.h) + 1
        self.W = (2*self.w) + 1 

    def generate(self):
        # Placeholder method for maze generation, to be implemented in subclasses
        return None

    def find_neighbours(self, r, c, grid, is_wall=False):
        # Find neighbouring cells with a given condition (e.g., being a wall)
        ns = []

        # Check if the cell above is a wall and is within the grid boundaries
        if r > 1 and grid[r - 2][c] == is_wall:
            ns.append((r - 2, c))
        # Check if the cell below is a wall and is within the grid boundaries
        if r < self.H - 2 and grid[r + 2][c] == is_wall:
            ns.append((r + 2, c))
        # Check if the cell to the left is a wall and is within the grid boundaries
        if c > 1 and grid[r][c - 2] == is_wall:
            ns.append((r, c - 2))
        # Check if the cell to the right is a wall and is within the grid boundaries
        if c < self.W - 2 and grid[r][c + 2] == is_wall:
            ns.append((r, c + 2))

        # Shuffle the list of neighbouring cells randomly
        shuffle(ns)
        return ns
