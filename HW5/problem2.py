import sys

myDict =  {'.': 'E', '..': 'I', '.-': 'A', '---': 'O', '..-': 'U'}

def codeDecryption(myCode, mySize):
   
    myList = [[0 for j in range(mySize)] for i in range(3)]


    for j in range(mySize):
        # print('1:', myCode[j: j + 1], '2:', myCode[j: j + 2], '3', myCode[j: j + 3])
        row1 = myCode[j: j + 1]
        row2 = myCode[j: j + 2]
        row3 = myCode[j: j + 3]
        
        if row1 in myDict:
            if j > 2:
                myList[0][j] =  myList[0][j - 1] +  myList[1][j - 2] + myList[2][j - 3]
            elif j > 1:
                myList[0][j] =  myList[0][j - 1] +  myList[1][j - 2]
            elif j > 0:
                myList[0][j] =  myList[0][j - 1]
            else:
                myList[0][j] = 1

            pass
        offset2 = mySize - 1
        if row2 in myDict and j < offset2:
            if j > 2:
                myList[1][j] =  myList[0][j - 1] +  myList[1][j - 2] + myList[2][j - 3]
            elif j > 1:
                myList[1][j] =  myList[0][j - 1] +  myList[1][j - 2]
            elif j > 0:
                myList[1][j] =  myList[0][j - 1]
            else:
                myList[1][j] = 1
            pass
        offset3 = offset2 - 1
        if row3 in myDict and j < offset3:
            if j > 2:
                myList[2][j] =  myList[0][j - 1] +  myList[1][j - 2] + myList[2][j - 3]
            elif j > 1:
                myList[2][j] =  myList[0][j - 1] +  myList[1][j - 2]
            elif j > 0:
                myList[2][j] =  myList[0][j - 1]
            else:
                myList[2][j] = 1
            pass

    myAns = myList[0][-1] + myList[1][-2] + myList[2][-3]
    print(myAns)   
    


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