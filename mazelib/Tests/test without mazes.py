import sys
from maze import Maze
from Wilsons import Wilsons
from BinaryTree import BinaryTree
from Ellers import Ellers
from Tremaux import Tremaux
from BackTrackingSolver import BacktrackingSolver
from BackTrackingGenerator import BacktrackingGenerator
from ShortestPath import ShortestPath
from RandomMouse import RandomMouse
import time
import numpy as np

# Function to get the number of mazes to generate
def get_loop_input():
    while True:
        try:
            loop = int(input("Enter the number of mazes: "))
            if loop <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return loop
        except ValueError:
            print("Please enter a valid integer.")

# Function to get user choice for clear or all paths taken
def get_clear_input():
    while True:
        clear_choice = input("Just solution or all paths taken? (True/False): ").strip().capitalize()
        if clear_choice in ["True", "False"]:
            return clear_choice == "True"
        else:
            print("Please enter either 'True' or 'False'.")

# Main function to run the test
def test():
    # Get user inputs for number of mazes and clear choice
    loop = get_loop_input()
    clear = get_clear_input()
    
    # Variables to track various statistics
    total_time = 0  
    total_len_solutions = 0  
    shortest_time = float('inf') 
    longest_time = 0  
    smallest_len_solutions = float('inf') 
    largest_len_solutions = 0  
    
    # Open a file to write results
    with open("mazes 25x25 test 1.txt", "w") as f:
        f.write("Maze Solution results:\n")
        
        # Lists of generators and solvers to iterate through
        generators = [BinaryTree, BacktrackingGenerator, Wilsons, Ellers]
        solvers = [Tremaux]
        
        # Iterate through each combination of generator and solver
        for generator in generators:
            for solver in solvers:
                # Write generator and solver names to file
                f.write(f"Generator: {generator.__name__}, Solver: {solver.__name__}\n")
                
                # Variables to track statistics for current generator-solver combination
                total_time_gen_solver = 0  
                total_len_solutions_gen_solver = 0
                shortest_time_gen_solver = float('inf')  
                longest_time_gen_solver = 0  
                smallest_len_solutions_gen_solver = float('inf')  
                largest_len_solutions_gen_solver = 0  
                
                # Generate mazes and solve
                for _ in range(loop):
                    m = Maze()
                    m.generator = generator(10, 10)
                    m.solver = solver()
                    m.generate()
                    m.generate_entrances()
                    start = time.time()
                    m.solve(clear=clear)
                    end = time.time()
                    time_taken = end - start
                    print(m)
                    
                    # Check if time exceeds 2 hours
                    if time_taken > 7200:  
                        print(f"Time taken for {generator.__name__}-{solver.__name__} mazes exceeded 2 hours. Exiting.")
                        break
                    
                    # Update statistics
                    shortest_time = min(shortest_time, time_taken)
                    longest_time = max(longest_time, time_taken)
                    total_time += time_taken
                    total_time_gen_solver += time_taken
                    shortest_time_gen_solver = min(shortest_time_gen_solver, time_taken)
                    longest_time_gen_solver = max(longest_time_gen_solver, time_taken)
                    
                    # Calculate number of solutions
                    num_solutions = sum(row.count('#') for row in m.tostring(solutions=True).split('\n'))
                    smallest_len_solutions = min(smallest_len_solutions, num_solutions)
                    largest_len_solutions = max(largest_len_solutions, num_solutions)
                    total_len_solutions += num_solutions
                    total_len_solutions_gen_solver += num_solutions
                    smallest_len_solutions_gen_solver = min(smallest_len_solutions_gen_solver, num_solutions)
                    largest_len_solutions_gen_solver = max(largest_len_solutions_gen_solver, num_solutions)
                
                # Calculate average statistics for current generator-solver combination
                average_time_gen_solver = total_time_gen_solver / loop if loop > 0 else 0
                average_len_solutions_gen_solver = total_len_solutions_gen_solver / loop if loop > 0 else 0
                
                # Write statistics to file
                f.write(f"Total time taken for {generator.__name__}-{solver.__name__} mazes: {total_time_gen_solver:.2f} seconds\n")
                f.write(f"Average time per {generator.__name__}-{solver.__name__} maze: {average_time_gen_solver:.2f} seconds\n")
                f.write(f"Shortest time taken for {generator.__name__}-{solver.__name__} mazes: {shortest_time_gen_solver:.2f} seconds\n")
                f.write(f"Longest time taken for {generator.__name__}-{solver.__name__} mazes: {longest_time_gen_solver:.2f} seconds\n")
                f.write(f"Total length of solutions for {generator.__name__}-{solver.__name__} mazes: {total_len_solutions_gen_solver}\n")
                f.write(f"Average length of solutions per {generator.__name__}-{solver.__name__} maze: {average_len_solutions_gen_solver:.2f}\n")
                f.write(f"Smallest length for solutions found for {generator.__name__}-{solver.__name__}: {smallest_len_solutions_gen_solver}\n")
                f.write(f"Largest number for solutions found for {generator.__name__}-{solver.__name__}: {largest_len_solutions_gen_solver}\n\n")

                # Check if time exceeded 2 hours, if so, exit
                if time_taken > 7200:
                    return

if __name__ == '__main__':
    test()
