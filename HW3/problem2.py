#  Using Recursion
# • Create a function that prints and counts the unique set of sub-strings of a given string
# • Input: abcab
# • Output: bca, bc, abc, cab, c, b, a, abca, ca, ab, abcab, bcab -> 12

def generateAllSubString(s, mySet):
    head = 0
    tail = len(s)
    if head == tail:
        return 1
    if s not in mySet:
        mySet.add(s)
    generateAllSubString(s[head: tail - 1], mySet)
    generateAllSubString(s[head + 1: tail], mySet)


myList = ['abcab', 'abc', 'racecar', 'Dream']

for e in myList:
    mySet = set()
    generateAllSubString(e, mySet)
    print(mySet)
    print(len(mySet))

