import numpy as np
from random import choice

from GenAlgo import genAlgo

class BinaryTree(genAlgo):
    def __init__(self, w, h, skew=None):
        super(BinaryTree, self).__init__(w, h)
        # Define skew options for biasing the maze generation direction
        skewes = {
            "NW": [(1, 0), (0, -1)],
            "NE": [(1, 0), (0, 1)],
            "SW": [(-1, 0), (0, -1)],
            "SE": [(-1, 0), (0, 1)],
        }
        # If a skew option is provided, use it; otherwise, choose one randomly
        if skew in skewes:
            self.skew = skewes[skew]
        else:
            key = choice(list(skewes.keys()))
            self.skew = skewes[key]

    def generate(self):
        # Create an empty array grid of dimensions HxW filled with walls (1s)
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)

        # Iterate over every second row and column in the grid
        for row in range(1, self.H, 2):
            for col in range(1, self.W, 2):
                # Carve out passages at every second row and column
                grid[row][col] = 0
                # Find the neighbouring cell according to the skew
                neighbour_row, neighbour_col = self.find_neighbour(row, col)
                # Carve out a passage at the neighbouring cell
                grid[neighbour_row][neighbour_col] = 0

        return grid

    def find_neighbour(self, current_row, current_col):
        # Initialize a list to store neighbouring cell coordinates
        neighbours = []
        # Iterate over each skew direction
        for b_row, b_col in self.skew:
            # Calculate the coordinates of the neighbouring cell
            neighbour_row = current_row + b_row
            neighbour_col = current_col + b_col
            # Check if the neighbouring cell is within the bounds of the grid
            if 0 < neighbour_row < (self.H - 1) and 0 < neighbour_col < (self.W - 1):
                # Add the neighbouring cell coordinates to the list
                neighbours.append((neighbour_row, neighbour_col))

        # If there are no valid neighbouring cells, return the current cell
        if len(neighbours) == 0:
            return (current_row, current_col)
        else:
            # Choose one of the valid neighbouring cells randomly and return its coordinates
            return choice(neighbours)
