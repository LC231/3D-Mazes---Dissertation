from random import choice

from SolveAlgo import solveAlgo

class BacktrackingSolver(solveAlgo):
    def _solve(self):
        # Initialize solution list
        solution = []
        # Start from the beginning of the maze
        current = self.start
        solution.append(current)

        # Continue until the current position is one cell away from the end
        while not self.one_away(solution[-1], self.end):
            # Get available neighbouring cells of the current position
            ns = self.available_neighbours(solution[-1])

            # If there are multiple available neighbours and the solution has progressed
            if len(ns) > 1 and len(solution) > 2:
                # Remove the cell that was visited two steps ago from the list of neighbours
                if solution[-3] in ns:
                    ns.remove(solution[-3])

            # Check if there are any available neighbours
            if len(ns) == 0:
                # No path available, return current solution
                break

            # Choose a random neighbouring cell to move to
            nxt = choice(ns)
            # Add the cell midway between the current cell and the chosen cell
            solution.append(self.midway(solution[-1], nxt))
            # Add the chosen cell to the solution path
            solution.append(nxt)

        # Return the solution path
        return [solution]

