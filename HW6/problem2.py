import sys


def currentExpSort(myList, exp):
    n = len(myList)
    output = [0] * (n)
    occurrences = [0] * (10)
    # occurences of each digit at that exponent
    for i in range(0, n):
        index = myList[i] // exp
        occurrences[index % 10] += 1
    

    # cumulative sum of occurences 
    # this will give us the position to place the integer of that digit occurence in the output array
    for i in range(1, 10): 
        occurrences[i] += occurrences[i - 1]
    

    i = n - 1
    while i >= 0:
        index = myList[i] // exp # This gives me the mod value at that exponent 9432 // 10 = 943
        # occurrences[index % 10] represents the number of occurrences at the index 943 mod 10 = 3
        # output[3 - 1]
        output[occurrences[index % 10] - 1] = myList[i] # placing all the integers that share the same digit occurence togther and in the digit occurrence order
        occurrences[index % 10] -= 1
        i -= 1
    # print(output)
    return output

def radixSort(myList):
    largestElement = myList[0]

    for i in range(len(myList)):
        if myList[i] > largestElement:
            largestElement = myList[i]
    

    exp = 1
    while largestElement / exp >= 1:
        myList = currentExpSort(myList, exp)
        exp *= 10

    print(myList)
    



if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        list1 = []
        list2 = []
        with open (fileName, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    length = line
                else:
                    myInts = line
            
            myList = myInts.split(' ')
            intList = list(map(int, myList))
            radixSort(intList)
            
      
       