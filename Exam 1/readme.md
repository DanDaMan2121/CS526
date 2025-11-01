## Problem1
Since we are given an array of cumulative totals, the sum total of any 3 consecutive days would be the value at the 3rd day relative to the current day minus the day before. This value is compared to the last value divided by 2 becuase the last value is the total snowfall. If that value is greater than half the total snowfall, the program returns true otherwise nothing is done. I loop through everyday until the second last day becuase if I make it to the second last day I can conclude there is no 3 consecutive days where the snowfall is greater than half the total snowfall.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem4.py .\testSymbolPuzzleGame\spg_input1.txt

## Problem2
My algorithm simulates the spread of infection across the grid by repeatedly checking each infected county and marking nearby counties as newly infected based on the 8 possible neighbor patterns. It keeps doing this day by day, adding new infections each round, until no new counties become infected. At that point, it returns the total number of infected counties, showing how far the virus spread before stabilizing.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem4.py .\testSymbolPuzzleGame\spg_input1.txt

## Problem3
My algorithm simulates moving through the aisles while keeping track of two baskets, each holding only one category of item. As I iterate through the items, it adds them to the appropriate basket if it matches the basket’s category or fills an empty basket. If a new category appears that doesn’t fit either basket, it clears one of the baskets (alternating between the two) and starts storing the new category. Throughout, it keeps track of the maximum number of items collected in the two baskets at any point and returns that as the result.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem4.py .\testSymbolPuzzleGame\spg_input1.txt

## Problem4
My algorithm checks whether a Sudoku board is valid by first creating lists of all rows, columns, and 3×3 matrices. It then iterates through each row, column, and sub matrix, counting the unique characters and comparing them to the expected set of values. If any duplicates are found in a row, column, or sub matrix, it marks the board as invalid; otherwise, it returns True, indicating the board follows the puzzle game rules.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem4.py .\testSymbolPuzzleGame\spg_input1.txt


