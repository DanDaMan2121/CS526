import sys

class DownHillSkier:
    def longestDecreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(row, col, prevVal):
            if row < 0 or row == rows or col < 0 or col == cols or matrix[row][col] <= prevVal:
                return 0
            if (row, col) in dp:
                return dp[(row, col)]

            res = 1
            # top row
            res = max(res, 1 + dfs(row + 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row + 1, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row + 1, col - 1, matrix[row][col]))

            # bottom row
            res = max(res, 1 + dfs(row - 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row - 1, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row - 1, col - 1, matrix[row][col]))

            # middle row
            res = max(res, 1 + dfs(row, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row, col - 1, matrix[row][col]))

            dp[(row, col)] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        return max(dp.values()) - 1 # offset
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        myMatrix = []
        with open(fileName, 'r') as file:
            for i, line in enumerate(file): 
                myLine = line.strip('\n')
                if i == 0:
                    myRow = int(myLine)
                elif i == 1:
                    myCol = int(myLine)
                else:
                   myList = myLine.split(' ')
                   myIntList = list(map(int, myList))
                   myMatrix.append(myIntList)
        mySolution = DownHillSkier()
        print(mySolution.longestDecreasingPath(myMatrix))
        # print(myMatrix)

                    


