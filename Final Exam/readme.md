## PROBLEM 1
My algorithm simulates flooding over time while cracks appear and are repaired, tracking whether the system stays safe or floods.

At each time step (count), new cracks may appear (from myDict), each adding water proportional to its crack size and being inserted into a max heap. One crack is repaired per step by popping the largest crack from the heap, reducing the incoming water rate. The algorithm updates the total water volume by adding the current inflow and subtracting a fixed village drain, ensuring the water level never goes below zero.

The max heap ensures the most dangerous crack is always fixed first, minimizing future water growth. The simulation ends when either the water exceeds a maximum safe level (FLOOD) or when all cracks are fixed and no more remain (SAFE).

DIRECTIONS: python .\problem1.py .\testFlood\flood_8.txts

## PROBLEM 2
My algorithm uses a depth-first search with memoization to explore all possible downhill moves from each cell. From a given cell, it recursively checks all 8 neighboring directions (up, down, left, right, and diagonals), but only moves to a cell with a lower value than the current one. Each cell’s best result is cached so it’s only computed once. Finally, it tries starting from every cell and returns the maximum path length found

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem2.py .\testSki\ski_input3.txt