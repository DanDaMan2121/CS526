## Problem 1

### ADD NODE
When you add a value, the tree checks whether it has a root.
If the root does not exist, the new value becomes the root.
If the tree already has nodes, the code compares the value to each node it visits:
it goes left when the value is smaller, right when the value is larger, and continues until it finds an empty spot where the new node can be inserted.
If the value is equal to an existing one, it does nothing and skips duplicates.

### FIND NODE
To find a value, the search starts at the root and compares the target value with the current node.
If the values match, it returns that node.
If the target value is smaller, it searches the left subtree; if it is larger, it searches the right subtree.
If it reaches a None child, that means the value is not in the tree.

### DELETE NODE
To delete a value, the tree first locates the node the same way it searches for a value.
If the node has no children, it is simply removed.
If it has one child, the node is replaced by its child.
If it has two children, the node’s value is replaced with the smallest value from its right subtree, and then that smallest value is removed from the right subtree to avoid duplication.
This ensures the tree stays a valid binary search tree.

### DIRECTIONS: Run the script.
ex. py .\problem1.py


## Problem 2
My algorithm scans the code one character at a time while tracking three possible states. Each state represents checking whether a vowel substring of length 1, 2, or 3 can begin at the current index. A matrix stores which vowel substrings are possible for each state at each position.

If a vowel of the current state’s length can be formed, the algorithm looks back at all valid previous states that could lead to this index. If none exist, it sets the matrix entry to 1; otherwise, it sets it to the sum of those previous state values. If a vowel cannot be formed, the matrix entry is 0. States whose vowel length exceeds the remaining characters are skipped.

After processing the entire code, the algorithm returns the sum of the final diagonal of the matrix, which represents the total number of vowel-substring combinations that can generate the given code.

### DIRECTIONS: Run the script while passing a test file as a command-line argument.
ex.  py .\problem2.py .\testVowel\vowel_input1.txt  


## Problem 3
This function finds the longest alternating increasing subsequence formed by switching between elements of arrays A and B. It uses dynamic programming: dpA[i] stores the best valid sequence ending at A[i], and dpB[j] stores the best sequence ending at B[j]. For every pair of positions, it checks whether a value from B can precede a value from A (or vice-versa) while preserving increasing index and value order. It builds longer sequences whenever possible, and at the end returns the longest sequence found.

### DIRECTIONS: Run the script while passing a test file as a command-line argument.
ex. py .\problem3.py .\testLongestSequence\longest_seq1.txt

