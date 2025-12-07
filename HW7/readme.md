## PROBLEM 1
The program starts by reading a text file and counting how many times each character appears, storing these frequencies in a dictionary. It then sorts the characters by frequency using a modified radix sort, from lowest to highest frequency. Each character is placed into a node, and all nodes are added to a priority queue that always retrieves the node with the smallest frequency first. Using these nodes, the program builds a Huffman tree by repeatedly combining the two nodes with the lowest frequencies into a new parent node until only the root node remains. Once the tree is built, the program traverses it in order to assign a unique binary code to each character, storing the mappings in dictionaries for encoding and decoding. It then encodes the original message into a compressed binary string using these codes. Finally, the program writes the compressed message to a file, reads it back, decodes it using the Huffman codes, and writes the decompressed text to another file.


DIRECTIONS: 
1. run the script while passing a test file as a command-line argument in the HW7 directory
2. type in a name for your compressed file when prompted. This will be moved to the compressedFiles folder after a name has been entered.
3. type in a name for your decompressed file when prompted. This will be moved to the decompressedFiles folder after a name has been entered.

ex. python .\problem1.py .\testFiles\testinput0.txt