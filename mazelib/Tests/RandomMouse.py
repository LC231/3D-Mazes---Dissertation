from random import choice  # Import the choice function for random selection

from SolveAlgo import solveAlgo  # Import the SolveAlgo class

class RandomMouse(solveAlgo):

    
    def _solve(self):        
        solution = []  # Initialize the solution path
        current = self.start
        # Add the starting position to the solution path
        solution.append(current)
        # Continue until the mouse reaches the end of the maze
        while not self.one_away(solution[-1], self.end):
            # Find available neighbours for the current position
            ns = self.available_neighbours(solution[-1])
            # Check if there are any available neighbours
            if len(ns) == 0:
                # No path available, return current solution
                break
            # Randomly select the next position from the available neighbours
            nxt = choice(ns)
            # Add the midpoint between the current position and the next position to the solution
            solution.append(self.midway(solution[-1], nxt))
            # Add the next position to the solution
            solution.append(nxt)
        # Return the solution path
        return [solution]
