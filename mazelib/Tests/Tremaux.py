from random import choice  
from SolveAlgo import solveAlgo  

class Tremaux(solveAlgo):  

    def __init__(self):  
        self.visited_cells = {}  # Dictionary to store visited cells and their visit counts

    def _solve(self):  
        self.visited_cells = {}
        solution = []
        current = self.start
        solution.append(current)
        self.visit(current)
        # Looping until reaching one cell away from the end
        while not self.one_away(solution[-1], self.end):
            # Getting available neighbours of the current cell
            ns = self.available_neighbours(solution[-1])
            # Choosing the next cell based on Tremaux algorithm
            nxt = self.next(ns, solution)
            # Adding the midpoint and the next cell to the solution path and marking the next cell as visited
            solution.append(self.midway(solution[-1], nxt))
            solution.append(nxt)
            self.visit(nxt)

        return [solution]  

    def visit(self, cell):  # Method to mark a cell as visited and update its visit count
        if cell not in self.visited_cells:
            self.visited_cells[cell] = 0  
        self.visited_cells[cell] += 1  # Increment visit count for the cell

    def get_visit_count(self, cell):  # get the visit count of a cell
        if cell not in self.visited_cells:
            return 0
        else:
            return self.visited_cells[cell] if self.visited_cells[cell] < 3 else 2  # Limiting visit count to 2

    def next(self, ns, solution):  #  determine the next cell to visit
        if len(ns) == 0:
            # No neighbours available, should not happen in a valid maze
            raise ValueError("No available neighbours found")
        if len(ns) == 1: 
            return ns[0]  

        visit_counts = {}  # Dictionary to store visit counts of neighbours
        for neighbour in ns:  # Iterating over available neighbours
            visit_count = self.get_visit_count(neighbour)  # Getting visit count for the neighbour
            if visit_count not in visit_counts:
                visit_counts[visit_count] = []  
            visit_counts[visit_count].append(neighbour)  # Adding neighbour to corresponding visit count list

        if 0 in visit_counts:  # If unvisited neighbours are available
            return choice(visit_counts[0])  # Return a randomly chosen unvisited neighbour
        elif 1 in visit_counts:  
            if len(visit_counts[1]) > 1 and len(solution) > 2 and solution[-3] in visit_counts[1]:
                visit_counts[1].remove(solution[-3])  # Removing backtracked neighbour if present
            return choice(visit_counts[1])  # Return a randomly chosen neighbour with one visit
        else:  
            if len(visit_counts[2]) > 1 and len(solution) > 2 and solution[-3] in visit_counts[2]:
                visit_counts[2].remove(solution[-3])  # Removing backtracked neighbour if present
            return choice(visit_counts[2])  
