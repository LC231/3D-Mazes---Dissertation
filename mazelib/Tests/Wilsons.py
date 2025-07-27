from random import choice, randrange  
import numpy as np  

from GenAlgo import genAlgo  


class Wilsons(genAlgo):  

    def __init__(self, w, h, hunt_type="random"): 
        super(Wilsons, self).__init__(w, h)  
        

    def generate(self):  
        
        # Creating an empty grid using numpy
        grid = np.empty((self.H, self.W), dtype=np.int8)
        grid.fill(1)  

        # Setting a random starting point in the grid
        grid[randrange(1, self.H, 2)][randrange(1, self.W, 2)] = 0
        num_visited = 1  # Number of cells visited initialized to 1
        row, col = self.chase(grid, num_visited)  # Getting initial coordinates for chase

        # Looping until no new cell can be visited
        while row != -1 and col != -1:
            walk = self.gen_rand_walk(grid, (row, col))  # Generating random walk path
            num_visited += self.solve_rand_walk(grid, walk, (row, col))  # Solving the walk and updating visited cells
            (row, col) = self.chase(grid, num_visited)  # Updating chase coordinates

        return grid  

    def chase(self, grid, count):  # determine the next cell to visit
        return self.random_chase(grid, count)  # Using random chase 

    def random_chase(self, grid, count):  # Method for random chase 
        if count >= (self.h * self.w):  
            return (-1, -1)  
        return (randrange(1, self.H, 2), randrange(1, self.W, 2))  

    def gen_rand_walk(self, grid, start):  # Method to generate a random walk path
        direction = self.rand_direction(start)  # Getting a random direction
        walk = {}  
        walk[start] = direction  # Setting initial direction in the walk
        current = self.move(start, direction)  # Moving to the next cell

        # Looping until a valid path is found
        while grid[current[0]][current[1]] == 1:
            direction = self.rand_direction(current)  # Getting a new random direction
            walk[current] = direction  # Setting direction in the walk
            current = self.move(current, direction)  # Moving to the next cell

        return walk  

    def rand_direction(self, current):  # Method to get a random direction from a cell
        r, c = current  # Extracting row and column from current cell coordinates
        options = []  # List to store available directions

        # Checking available directions and adding them to options list
        if r > 1:
            options.append(0)  # North
        if r < (self.H - 2):
            options.append(1)  # South
        if c > 1:
            options.append(2)  # East
        if c < (self.W - 2):
            options.append(3)  # West

        direction = choice(options)  # Choosing a random direction from available options
        if direction == 0:
            return (-2, 0)  # North
        elif direction == 1:
            return (2, 0)  # South
        elif direction == 2:
            return (0, -2)  # East
        else:
            return (0, 2)  # West

    def move(self, start, direction):  # move from one cell to another
        return (start[0] + direction[0], start[1] + direction[1])  # Calculating new coordinates after movement

    def solve_rand_walk(self, grid, walk, start):  # solve the random walk path
        visits = 0  # Counter for visited cells
        current = start  # Setting current cell to starting cell

        # Looping until reaching an already visited cell
        while grid[current[0]][current[1]] != 0:
            grid[current] = 0  # Marking the current cell as visited
            next1 = self.move(current, walk[current])  # Moving to the next cell based on walk direction
            # Marking the wall cell between current and next cell as visited
            grid[(next1[0] + current[0]) // 2, (next1[1] + current[1]) // 2] = 0
            visits += 1  
            current = next1  

        return visits  
