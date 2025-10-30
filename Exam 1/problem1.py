import sys




fileName = 'testSnowFall/snowfall_input5.txt'

# cleanSet = set()
myList = []


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i > 0:
            newLine = line.strip('\n')
            myList.append(newLine)
myList = myList[0].split(' ')
intList = list(map(int, myList))


def myFunction (list):
    length = len(list)
    val = list[-1]
    compare = val / 2
    for i in range(length):
        if length < 3:
            return False
        if i > length - 3:
            return False
        else:
            if i == 0:
                v1 = 0
            else:
                v1 = list[i - 1]
            total = list[i + 2] - v1
            if total > compare:
                return True
        


print(intList)
ans = myFunction(intList)

if ans:
    print('YES')
else:
    print('NO')
