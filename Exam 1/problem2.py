
fileName = './testPandemic/pandemic_input1.txt'
myList = []


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i > 0:
            newLine = line.strip('\n')
            myList.append(newLine)

myArray = [
    ['h', 'h', 'h', 'h', 'h'],
    ['h', 'h', 'h', 'h', 'h'],
    ['h', 'h', 'h', 'h', 'h'],
    ['h', 'h', 'h', 'h', 'h'],
    ['h', 'h', 'h', 'h', 'h']
]

length = len(myList)
pointList = []
for i in range(length):
    x, y = list(map(int, myList[i].split(' ')))
    pointList.append((x, y))
    myArray[x][y] = 'i'


newPoints = len(pointList)
infectedTotal = newPoints
print(pointList)
while newPoints > 0:
    newList = []
    for e in pointList:
        x = e[0]
        y = e[1]
        # print(x, y)
        isInfected = 'i'
        try:
            if isInfected == myArray[x][y + 2]: # checked
                if myArray[x][y + 1] != 'i':
                    myArray[x][y + 1] = 'i'
                    newList.append((x, y + 1))
        except IndexError:
            pass
        try:
            if isInfected ==  myArray[x - 1][y + 1] and x - 1 > -1:
                if myArray[x][y + 1] != 'i':
                    myArray[x][y + 1] = 'i'
                    newList.append((x, y + 1))
                if myArray[x - 1][y] != 'i':
                    myArray[x - 1][y] = 'i'
                    newList.append((x - 1, y))
                
        except IndexError:
            pass
        try:
            if isInfected == myArray[x + 1][y + 1]: # checked
                if myArray[x][y + 1] != 'i':
                    myArray[x][y + 1] = 'i'
                    newList.append((x, y + 1))
                if myArray[x + 1][y] != 'i':
                    myArray[x + 1][y] = 'i'
                    newList.append((x + 1, y))
        except IndexError:
            pass
        try:
            if isInfected == myArray[x - 2][y] and x - 2 > -1: # checked
                if myArray[x - 1][y] != 'i':
                    myArray[x - 1][y] = 'i'
                    newList.append((x - 1, y))
        except IndexError:
            pass
        try:
            if isInfected ==  myArray[x + 2][y]: # checked
                if myArray[x + 1][y] != 'i':
                    myArray[x + 1][y] = 'i'
                    newList.append((x + 1, y))
        except IndexError:
            pass
        try:
            if isInfected ==  myArray[x - 1][y - 1] and x - 1 > -1 and y - 1 > -1:
                if myArray[x - 1][y] != 'i':
                    myArray[x - 1][y] = 'i'
                    newList.append((x - 1, y))
                if myArray[x][y - 1] != 'i':
                    myArray[x][y - 1] = 'i'
                    newList.append((x, y - 1))
        except IndexError:
            pass
        try:
            if isInfected ==  myArray[x + 1][y  - 1] and y - 1 > -1:
                if myArray[x + 1][y] != 'i':
                    myArray[x + 1][y] = 'i'
                    newList.append((x + 1, y))
                if myArray[x][y - 1] != 'i':
                    myArray[x][y - 1] = 'i'
                    newList.append((x, y - 1))

        except IndexError:
            pass
        try:
            if isInfected ==  myArray[x][y - 2] and y - 2 > -1: # checked
                if myArray[x][y - 1] != 'i':
                    myArray[x][y - 1] = 'i'
                    newList.append((x, y - 1))
        except IndexError:
            pass
    
    newPoints = len(newList)
    infectedTotal += newPoints
    pointList = newList
        

# print(pointList)
print(infectedTotal)
print(myArray)
if infectedTotal < 25:
    print('There are healthy counties')
else:
    print('There are no healthy counties')

