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


folderPath = '/testpalendrome'

def palindrome(s):
    head = 0
    tail = len(s) - 1
    while head < tail:
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1
    return True


for fileName in os.listdir(folderPath)
    if fileName.endswith('.txt'):
        filePath = os.path.join(folderPath, fileName)
        with open(filePath, 'r') as file:
            for line in file:
                palindrome(line)
                print('ding')