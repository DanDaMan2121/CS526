import math
fileName = './testSymbolPuzzleGame/spg_input2.txt'
myList = []


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i == 0:
            n = int(line)
        else:
            newLine = line.strip('\n')
            myList.append(newLine)
# myList = myList[0].split(',')
rows = []

for e in myList:
    row = e.split(',')
    rows.append(row)

cols = []
length = len(rows) - 1
for i in range(length):
    col = []
    # print(rows[i][1])
    for j in range(length):
        val = rows[j][i]
        col.append(val)
    cols.append(col)
rootLength = int(math.sqrt(n))
# print(rootLength)
subMatrix = []
for i in range(rootLength):
    for j in range(rootLength):
        matrix = []
        for k in range(rootLength):
            for l in range(rootLength):
                val = rows[k + (i * rootLength)][l + (j * rootLength)]
                matrix.append(val)
        subMatrix.append(matrix)
# print(subMatrix)

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
        print('row #', i, rows[i])
        isClean = False
        break
print('Rows:', isClean)
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
        print('col #', i, cols[i])

        isClean = False
        break
print('Cols:', isClean)
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
        print('matrix', i,  subMatrix[i])
        isClean = False
        break
print('subMatrix:', isClean)