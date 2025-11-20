# 3D Maze Generation and Solving Library

A Python library for generating and solving procedural mazes using various algorithms.

## Features

### Maze Generators
- **BacktrackingGenerator**: Recursive backtracking algorithm
- **BinaryTree**: Binary tree algorithm with configurable skew
- **Ellers**: Eller's algorithm with horizontal/vertical skew
- **Wilsons**: Wilson's algorithm for uniform spanning trees

### Maze Solvers
- **RandomMouse**: Simple random walk solver
- **Tremaux**: Tremaux's algorithm (marks visited cells)
- **BacktrackingSolver**: Backtracking-based solver
- **ShortestPath**: Finds all shortest paths using breadth-first approach

## Usage

### Basic Example

```python
from maze import Maze
from BackTrackingGenerator import BacktrackingGenerator
from Tremaux import Tremaux

# Create a maze instance
m = Maze()
m.generator = BacktrackingGenerator(25, 25)
m.solver = Tremaux()

# Generate and solve
m.generate_and_solve()

# Print the maze
print(m)
```

### Using the Menu Interface

```python
from menu import generate_solve_and_show

generate_solve_and_show()
```

## Code Structure

- `maze.py`: Main Maze class for coordinating generation and solving
- `GenAlgo.py`: Base class for maze generators
- `SolveAlgo.py`: Base class for maze solvers
- `constants.py`: Centralized constants and configuration
- `utils.py`: Utility functions for common operations
- `__init__.py`: Package initialization and exports

## Recent Improvements

### Code Quality
- ✅ Added comprehensive docstrings to all classes and methods
- ✅ Added type hints for better IDE support and code clarity
- ✅ Created constants file to eliminate magic numbers
- ✅ Added utility functions for common operations
- ✅ Improved error handling and validation

### Bug Fixes
- ✅ Fixed BackTrackingGenerator to randomly choose neighbors
- ✅ Fixed Wilsons direction mapping (East/West were swapped)
- ✅ Added bounds checking to prevent IndexErrors
- ✅ Fixed infinite recursion in entrance generation
- ✅ Improved solution cleaning algorithm efficiency

### Architecture
- ✅ Created proper package structure with `__init__.py`
- ✅ Separated concerns with utility modules
- ✅ Added fallback imports for backward compatibility

## Constants

The `constants.py` file centralizes all magic numbers and configuration:
- Grid cell types (WALL, PASSAGE, UNVISITED)
- Grid structure constants (WALL_MULTIPLIER, WALL_OFFSET)
- Minimum dimensions and validation thresholds
- String representation characters
- Algorithm-specific constants

## Testing

Run tests using the provided test scripts:
- `test with mazes.py`: Tests with pre-generated mazes
- `test without mazes.py`: Tests with dynamically generated mazes

## Requirements

- Python 3.6+
- numpy
- matplotlib (for visualization)

## License

This code is part of a dissertation project on 3D maze generation and solving.

