import sys
def myFunction (list):
    length = len(list)
    if length < 3:
        return False
    val = list[-1]
    compare = val / 2
    for i in range(length):
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
        


if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        myList = []
        myLine = ''
        with open (fileName, 'r') as file: 
            for i, line in enumerate(file):
                if i > 0:
                    myLine += line
                    newLine = line.strip('\n')
                    myList.append(newLine)
        myList = myList[0].split(' ')
        intList = list(map(int, myList))


    ans = myFunction(intList)
    if ans:
        print(myLine, 'solution: yes')
    else:
        print(myLine, 'solution: no')
