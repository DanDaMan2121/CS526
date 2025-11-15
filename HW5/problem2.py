import sys

myDict =  {'.': 'E', '..': 'I', '.-': 'A', '---': 'O', '..-': 'U'}

def codeDecryption(myCode, mySize):
    # 3 rows for vowel substrings of length 1, 2, and 3
    dp = [[0] * mySize for _ in range(3)]

    # Helper: compute DP update for a given row and index
    def update(row, j):
        length = row + 1  # row 0 = length 1, row 1 = length 2, row 2 = length 3
        substr = myCode[j:j + length]

        # substring must exist in dictionary AND must fit inside code
        if substr not in myDict or j + length > mySize:
            return 0

        # base case: starting at index 0
        if j == 0:
            return 1

        total = 0
        # Add contributions from previous valid states
        if j - 1 >= 0: total += dp[0][j - 1]
        if j - 2 >= 0: total += dp[1][j - 2]
        if j - 3 >= 0: total += dp[2][j - 3]
        return total

    # Fill DP table
    for j in range(mySize):
        for row in range(3):
            dp[row][j] = update(row, j)

    # Final answer = sum of last valid diagonal
    ans = 0
    if mySize - 1 >= 0: ans += dp[0][mySize - 1]
    if mySize - 2 >= 0: ans += dp[1][mySize - 2]
    if mySize - 3 >= 0: ans += dp[2][mySize - 3]

    print('The Number of Vowel combinations is:', ans)

    


if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        
        with open (fileName, 'r') as file:
           for i, line in enumerate(file):
                if i == 0:
                   tempLine = line.strip('\n')
                   mySize = int(tempLine)
                else:
                   myCode = line.strip('\n')

        codeDecryption(myCode, mySize)