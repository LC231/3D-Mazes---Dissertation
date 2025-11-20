import numpy as np
from random import randrange, choice

from GenAlgo import genAlgo

class BacktrackingGenerator(genAlgo):
    def __init__(self, w, h):
        super(BacktrackingGenerator, self).__init__(w, h)

    def generate(self):
        # Create an empty grid of dimensions HxW filled with walls (1s)
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)

        # Choose a random starting point (odd row and column indices)
        crow = randrange(1, self.H, 2)
        ccol = randrange(1, self.W, 2)
        # Mark the starting point as a passage (0)
        grid[crow][ccol] = 0

        # Initialize a stack to keep track of visited cells
        track = [(crow, ccol)]

        # Main loop to generate the maze
        while track:
            # Get the current cell's coordinates
            (crow, ccol) = track[-1]
            # Find neighbouring cells that are walls
            neighbours = self.find_neighbours(crow, ccol, grid, True)

            # If no unvisited neighbouring cells, backtrack
            if len(neighbours) == 0:
                track = track[:-1]  # Remove the current cell from the track
            else:
                # Choose a random neighbouring cell and mark it as a passage
                nrow, ncol = choice(neighbours)
                grid[nrow][ncol] = 0
                # Mark the cell between current and chosen cell as passage
                grid[(nrow + crow) // 2][(ncol + ccol) // 2] = 0
                # Move to the chosen neighbouring cell
                track.append((nrow, ncol))

        return grid
