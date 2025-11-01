import math
import sys

def isValidPuzzle(myList):
    # Generate rows
    rows = []
    for e in myList:
        row = e.split(',')
        rows.append(row)

    # Generate cols
    cols = []
    length = len(rows)
    for i in range(length):
        col = []
        # print(rows[i][1])
        for j in range(length):
            val = rows[j][i]
            col.append(val)
        cols.append(col)
    
    # Generate subMatrix
    n = len(myList)
    rootLength = int(math.sqrt(n))
    subMatrix = []
    for i in range(rootLength):
        for j in range(rootLength):
            matrix = []
            for k in range(rootLength):
                for l in range(rootLength):
                    val = rows[k + (i * rootLength)][l + (j * rootLength)]
                    matrix.append(val)
            subMatrix.append(matrix)
    
    # Test rows
    isClean = True
    for i in range(length):
        count = 0
        myDict = dict()
        for j in range(length):
            val = rows[i][j]
            if val not in myDict:
                myDict[val] = 0
                count += 1
        checkDupe = set(rows[i])
        setLen = len(checkDupe)
        if count != setLen:
            # print('row #', i, rows[i]) # Get row error #
            isClean = False
            break
    # print('Rows:', isClean) # Get rows validity

    # Test cols
    for i in range(length):
        count = 0
        myDict = dict()
        for j in range(length):
            val = cols[i][j]
            if val not in myDict:
                myDict[val] = 0
                count += 1
            else:
                if val != '.':
                    count += 1
        checkDupe = set(cols[i])
        setLen = len(checkDupe)
        if count != setLen:
            # print('col #', i, cols[i]) # Get col error #

            isClean = False
            break
    # print('Cols:', isClean) # Get cols validity
    
    # Test subMatrix
    for i in range(length):
        count = 0
        myDict = dict()
        for j in range(length):
            val = subMatrix[i][j]
            if val not in myDict:
                myDict[val] = 0
                count += 1
            else:
                if val != '.':
                    count += 1
        checkDupe = set(subMatrix[i])
        setLen = len(checkDupe)
        if count != setLen:
            # print('matrix', i,  subMatrix[i]) # get matrix error #
            isClean = False
            break
    # print('subMatrix:', isClean) # Get subMatrix validity
    return isClean


if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        myList = []
        with open (fileName, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    n = line.strip('\n')
                elif i == 1:
                    validSymbols = line.strip('\n')
                else:
                    newLine = line.strip('\n')
                    myList.append(newLine)
        validity = isValidPuzzle(myList)
        if validity:
            print('The board is valid')
        else:
            print('The board is invalid')