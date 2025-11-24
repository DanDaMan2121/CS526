import sys


# Merge Sort
def mergeSort(myList):
    myList = myList.copy()

    if len(myList) <= 1:
        return myList

    mid = len(myList) // 2
    left = mergeSort(myList[:mid])
    right = mergeSort(myList[mid:])

    sortedList = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1

    sortedList.extend(left[i:])
    sortedList.extend(right[j:])
    return sortedList


# Quick Sort
def quickSort(myList):
    if len(myList) <= 1:
        return myList.copy()

    pivot = myList[-1]  
    left = [x for x in myList[:-1] if x <= pivot]
    right = [x for x in myList[:-1] if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)




def insertionSort(myList):
    sortedList = myList.copy()

    for i in range(1, len(sortedList)):
        key = sortedList[i]
        j = i - 1

        while j >= 0 and sortedList[j] > key:
            sortedList[j + 1] = sortedList[j]
            j -= 1

        sortedList[j + 1] = key

    return sortedList



if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]

        size = 0
        myList = []
        with open(fileName, 'r') as file:
            for i, line in enumerate(file):
                myLine = line.strip('\n')
                if i == 0:
                    size = int(myLine)
                else:
                    myList = list(map(int, myLine.split(' ')))
            
            print(f"Unsorted list: {myList}")

            mSort = mergeSort(myList)
            print(f"MergeSort: {mSort}")
            
            qSort = quickSort(myList)
            print(f"QuickSort: {qSort}")
            
            iSort = insertionSort(myList)
            print(f"InsertSort: {iSort}")
                    