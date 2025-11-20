from SolveAlgo import solveAlgo  # Import the solveAlgo class

class ShortestPath(solveAlgo):
    # ShortestPaths class inherits from solveAlgo class
   
    def _solve(self):
        
        start = self.start

        # Find available neighbour positions from the start position
        start_posis = self.available_neighbours(start)
        solutions = []
        # Iterate through possible start positions
        for sp in start_posis:
            solutions.append([self.midway(start, sp), sp])

        # Count the number of unfinished solutions
        num_unfinished = len(solutions)


        while num_unfinished > 0:
            # Iterate through solutions
            for s in range(len(solutions)):
                # If the last position repeats or reaches the end position, mark it as None
                if solutions[s][-1] in solutions[s][:-1]:
                    solutions[s].append(None)
                elif self.one_away(solutions[s][-1], self.end):
                    solutions[s].append(None)
                elif solutions[s][-1] is not None:
                    # Check if we've reached the end (one cell away)
                    if self.one_away(solutions[s][-1], self.end):
                        solutions[s].append(None)
                        continue

                    # Find available neighbour positions from the last position
                    ns = self.available_neighbours(solutions[s][-1])
                    ns = [n for n in ns if n not in solutions[s][-2:]]

                    if len(ns) == 0:
                        solutions[s].append(None)
                    elif len(ns) == 1:
                        solutions[s].append(self.midway(ns[0], solutions[s][-1]))
                        solutions[s].append(ns[0])
                    else:
                        for j in range(1, len(ns)):
                            nxt = [self.midway(ns[j], solutions[s][-1]), ns[j]]
                            solutions.append(list(solutions[s]) + nxt)
                        solutions[s].append(self.midway(ns[0], solutions[s][-1]))
                        solutions[s].append(ns[0])

            # Update the number of unfinished solutions
            num_unfinished = sum(map(lambda sol: 0 if sol[-1] is None else 1, solutions))

        # Clean the solutions and remove duplicate solutions
        solutions = self.clean(solutions)
        return solutions

    def clean(self, solutions):
        # Method to clean up the solutions by removing unnecessary paths
        
        new_solutions = []
        for sol in solutions:
            if not sol or sol[-1] is None:
                # Solution didn't reach the end, skip it
                continue
                
            new_sol = list(sol)
            
            # Remove the None marker if present
            if new_sol and new_sol[-1] is None:
                new_sol = new_sol[:-1]
            
            # If solution ends one cell away from end, we might need to adjust
            if len(new_sol) > 1 and self.one_away(new_sol[-1], self.end):
                # Solution is valid, keep it
                pass
            elif len(new_sol) > 2 and self.one_away(new_sol[-2], self.end):
                # Remove the last cell if it's not needed
                new_sol = new_sol[:-1]
            
            # Remove end point if it's explicitly in the solution
            if new_sol and new_sol[-1] == self.end:
                new_sol = new_sol[:-1]
                
            if new_sol:
                new_solutions.append(new_sol)

        # Remove duplicate solutions
        solutions = self.rem_dupe_sols(new_solutions)

        return sorted(solutions, key=len)

    def rem_dupe_sols(self, sols):
        # Method to remove duplicate solutions
        
        return [list(s) for s in set(map(tuple, sols))]
