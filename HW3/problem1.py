# Problem 1

# Write a program to determine if a given string is a palindrome
# • Input: you will be given an input file with one string per line
# • Output: for each line output if the string is a palindrome
# • Output: the total number of palindromes
# • E.g.
# • Input:
# geek
# asleelsa
# thisisatesttsetasisiht
# • Output:
# false
# true
# true
# 2



import os


folderName = './testPalendrome'

def palindrome(s):
    head = 0
    tail = len(s) - 1
    while head < tail:
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1
    return True

myAns = []

for fileInFolder in os.listdir(folderName):
    fileName = folderName + '/' + fileInFolder
    with open(fileName, 'r') as file:
        myTestResults = []
        count = 0
        for line in file:
            newLine = line.strip('\n')
            if palindrome(newLine):
                myTestResults.append('True')
                count += 1
            else:
                myTestResults.append('False')
        myTestResults.append(count)
        myAns.append(myTestResults)

fileCount = 0
folderName = './ansPalendrome'
for fileInFolder in os.listdir(folderName):
    fileName = folderName + '/' + fileInFolder
    with open(fileName, 'r') as file:
        count = 0
        for line in file:
            newLine = line.strip('\n')
            if newLine != str(myAns[fileCount][count]):
                print('Error on file:', fileCount, 'line:', count, 'ans:', newLine, "myAns:", myAns[fileCount][count])
                break
            count += 1
    print('File:', fileCount, 'passed with no problems!')
    fileCount += 1

