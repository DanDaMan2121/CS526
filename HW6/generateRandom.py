import random
def generateInput(fileName):
    val = input("enter the number of random ints: ")
    with open(fileName, 'w') as f:
        f.write(val + '\n') 
        myRange = int(val)
        for i in range(myRange):
            myInt = random.randint(0, 1000)
            myStr = str(myInt)
            if i != myRange - 1:
                myStr = myStr + ' '
            f.write(myStr)

fileName = input('please type the file name: ')
generateInput(fileName)
print('ran')