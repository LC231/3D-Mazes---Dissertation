import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from maze import Maze  
from Wilsons import Wilsons  
from BinaryTree import BinaryTree  
from Ellers import Ellers  
from Tremaux import Tremaux  
from BackTrackingSolver import BacktrackingSolver  
from BackTrackingGenerator import BacktrackingGenerator  
from ShortestPath import ShortestPath
from RandomMouse import RandomMouse  

def get_user_input(depth):
    # Function to get user input for maze generation and solving options
    generator_options = {
        "1": Wilsons,
        "2": BinaryTree,
        "3": Ellers,
        "4": BacktrackingGenerator
    }
    solver_options = {
        "1": RandomMouse,
        "2": Tremaux,
        "3": BacktrackingSolver,
        "4": ShortestPath
    }
    while True:
        print("Select a generator:")
        for key, value in generator_options.items():
            print(key, value.__name__)

        generator_choice = input("Enter the number of your choice: ")
        if generator_choice in generator_options:
            break
        else:
            print("Invalid input! Please enter a valid generator choice.")

    while True:
        width_input = input("Enter the width for the maze: ")
        if width_input.isdigit():
            width = int(width_input)
            break
        else:
            print("Invalid input! Please enter a valid integer for width.")

    while True:
        height_input = input("Enter the height for the maze: ")
        if height_input.isdigit():
            height = int(height_input)
            break
        else:
            print("Invalid input! Please enter a valid integer for height.")

    while True:
        print("Select a solver:")
        for key, value in solver_options.items():
            print(key, value.__name__)

        solver_choice = input("Enter the number of your choice: ")
        if solver_choice in solver_options:
            break
        else:
            print("Invalid input! Please enter a valid solver choice.")

    return [(generator_options[generator_choice](width, height), solver_options[solver_choice]()) for _ in range(depth)]



def generate_solve_and_show():
    # Function to generate, solve, and show mazes
    while True:
        depth_input = input("Enter the number for the depth/amount of mazes: ")
        if depth_input.isdigit():
            depth = int(depth_input)
            break
        else:
            print("Invalid input! Please enter a valid integer for depth.")

    # Get user choices for maze generation and solving
    choices = get_user_input(depth)

    clear = True  # Default value

    clear_choice = input("Just solution or all paths taken? (True/False): ").capitalize()  # Convert input to capital case
    while clear_choice not in ["True", "False"]:
        print("Invalid input! Please enter either 'True' or 'False'.")
        clear_choice = input("Just solution or all paths taken? (True/False): ").capitalize()  # Ask again if input is invalid

    if clear_choice == "False":
        clear = False

    # Generate, solve, and show each maze
    for generator, solver in choices:
        m = Maze()
        m.generator = generator
        m.solver = solver
        m.generate_and_solve(clear=clear)
        visualize(m.grid, m.start, m.end, m.solutions)

def visualize(grid, start=None, end=None, solutions=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Initialize empty list to store walls (circles representing walls)
    walls = []
    

    # Animation function to update plot
    def animate(frame):
        i, j = divmod(frame, grid.shape[1])
        if grid[i, j] == 1:
            wall = ax.plot(j, i, marker='s', markersize=10, color='black')[0]
            walls.append(wall)
        return walls

    # Total frames for animation (equal to number of elements in grid)
    total_frames = grid.size

    # Create animation object and display it
    ani = FuncAnimation(fig, animate, frames=total_frames, interval=1, blit=True)

    # Show the grid animation
    plt.show()
    
    # Plot solutions if provided after grid animation
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(grid, cmap=plt.cm.binary, interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Plot start and end points if provided
    if start is not None:
        ax.scatter(start[1], start[0], marker='o', s=50, color='green')
    if end is not None:
        ax.scatter(end[1], end[0], marker='o', s=50, color='red')
    
    # Plot solutions if provided
    if solutions is not None:
        flat_solutions = [item for sublist in solutions for item in sublist]
        path_x, path_y = zip(*flat_solutions)  
        
        # Plot solution before clearing in red dots
        ax.plot(path_y, path_x, marker='o', markersize=5, color='purple', linestyle='None')
        
        # Plot cleared solution in cyan dots
        line, = ax.plot([], [], marker='o', markersize=5, color='cyan', linestyle='None')  

        # Initialize dot to show current position in solution array
        dot, = ax.plot([], [], marker='o', markersize=5, color='black', linestyle='None')

        # Define initialization function for animation
        def init():
            line.set_data([], [])
            dot.set_data([], [])
            return line, dot

        # Define update function for animation
        def update(frame):
            line.set_data(path_y[:frame], path_x[:frame])
            dot.set_data(path_y[frame], path_x[frame])
            return line, dot

        # Create animation object and display it
        ani = FuncAnimation(fig, update, frames=len(path_x), init_func=init, blit=True)
        plt.show()

if __name__ == '__main__':
    generate_solve_and_show()
