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
from memory_profiler import profile
import numpy as np

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

def get_clear_input():
    while True:
        clear_choice = input("Just solution or all paths taken? (True/False): ").strip().capitalize()
        if clear_choice in ["True", "False"]:
            return clear_choice == "True"
        else:
            print("Please enter either 'True' or 'False'.")
@profile
def test():
    loop = get_loop_input()
    clear = get_clear_input()
    total_time = 0  # Variable to accumulate the total time
    total_len_solutions = 0
    shortest_time = float('inf')  # Variable to track the smallest time
    longest_time = 0  # Variable to track the largest time
    smallest_len_solutions = float('inf')  # Variable to track the smallest number of solutions
    largest_len_solutions = 0  # Variable to track the largest number of solutions
    
    
    with open("25x25 test 1.txt", "a") as f: #change to "a" so that the data can be saved
        f.write("Maze Solution results:\n")
        
        for _ in range(loop):
            m = Maze()
            m.generator = Wilsons(25, 25)
            m.solver = Tremaux()
            m.generate()
            m.generate_entrances()
            start = time.time()
            m.solve(clear=clear)
            end = time.time()
            time_taken = end - start
            print(m)

            
            shortest_time = min(shortest_time, time_taken)
            longest_time = max(longest_time, time_taken)
            # Accumulate the total time
            total_time += time_taken
            
            # Calculate number of solutions
            num_solutions = sum(row.count('#') for row in m.tostring(solutions=True).split('\n'))
            smallest_len_solutions = min(smallest_len_solutions, num_solutions)
            largest_len_solutions = max(largest_len_solutions, num_solutions)
            total_len_solutions += num_solutions

            # Write time and total number of solutions to file

        f.write(f"Total time taken for mazes: {total_time:.2f} seconds\n")
        average_time = total_time / loop if loop > 0 else 0
        f.write(f"Average time per maze: {average_time:.2f} seconds\n")
        f.write(f"Shortest time taken for a maze: {shortest_time:.2f} seconds\n")
        f.write(f"Longest time taken for a maze: {longest_time:.2f} seconds\n")

        average_len_solutions = total_len_solutions / loop if loop > 0 else 0
        f.write(f"Total length of solutions for all mazes: {total_len_solutions}\n")
        f.write(f"Average length of solutions per maze: {average_len_solutions:.2f}\n")
        f.write(f"Smallest length for solutions found: {smallest_len_solutions}\n")
        f.write(f"Largest length for solutions found: {largest_len_solutions}\n")


if __name__ == '__main__':
    test()





