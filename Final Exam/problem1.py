import sys
import heapq
myDict = dict()



class MaxHeap:
    def __init__(self):
        # We use a min-heap internally
        self._heap = []

    def push(self, item):
        # Negate the item's value before pushing to simulate max-heap behavior
        heapq.heappush(self._heap, -item)

    def pop(self):
        # Pop the smallest (negative largest) item and negate it back
        if not self.is_empty():
            return -heapq.heappop(self._heap)
        return None

    def peek(self):
        # Peek at the largest item without removing it
        if not self.is_empty():
            return -self._heap[0]
        return None
        
    def is_empty(self):
        return len(self._heap) == 0
    
    def step(self, val):
        for i in range(len(self._heap)):
            self._heap[i] -= val
    def size(self):
        return len(self._heap)


class Crack:
    def __init__(self, time=0, size=0):
        self.timeUnit = time    # guaranteed to be non-negative integer
        self.crackSize = size   # guaranteed to be a positive integer
    def __str__(self):
        return f'the time unit the crack appears: {self.timeUnit} initial size of crack: {self.crackSize}'
    def __repr__(self):
        return f'Crack({self.crackSize})'
    
def village(threshold, drain):
    totalWater = 0
    maxWater = 0
    waterFlow = 0
    count = 0
    previousKey = None

    myHeap = MaxHeap()
    
    for key in myDict:
        myList = myDict[key]
        if previousKey != None:
            # print(f'Key: {key} PreviousKey: {previousKey}')
            diff = int(key) - int(previousKey) - 1

            for i in range(diff):
                # waterFlow at current time
                if count != 0:
                    myLargestValue = myHeap.pop()
                    waterFlow -= myLargestValue
                    count -= 1
                    totalWater += waterFlow - drain
                    # print(f'totalWater: {totalWater} at time:{int(previousKey) + i}')
                    # next round prep
                    waterFlow += count
                    myHeap.step(1)
                else:
                    # print('offset')
                    timeMultipler = diff - i
                    totalWater -= (drain * timeMultipler)
                    if totalWater < 0:
                        totalWater = 0
                    # print(f'totalWater: {totalWater} at time:{int(previousKey) + i}')
                    break
                
                if totalWater >= threshold:
                    return f'FLOOD\n{int(previousKey) + i + 1}\n{totalWater}'
                if totalWater > maxWater:
                    maxWater = totalWater            
        
        # this gets me the value at time t
        for e in myList:
            count += 1
            waterFlow += int(e.crackSize)
            myHeap.push(int(e.crackSize))
        # everytime we pop we subtract from the count and from the waterFlow
        myLargestValue = myHeap.pop()
        waterFlow -= myLargestValue
        count -= 1

        totalWater += waterFlow - drain
        if totalWater < 0:
            totalWater = 0
        # print(f'totalWater: {totalWater} at time:{int(key)}')

        if totalWater >= threshold:
            return f'FLOOD\n{key}\n{totalWater}'
        if totalWater > maxWater:
            maxWater = totalWater

        waterFlow += count
        myHeap.step(1)
        previousKey = key

    length = count
    for i in range(length):
        myLargestValue = myHeap.pop()
        waterFlow -= myLargestValue
        count -= 1
        totalWater += waterFlow - drain

        # next round prep
        waterFlow += count
        myHeap.step(1)

        if totalWater >= threshold:
            return f'FLOOD\n{int(previousKey) + i + 1}\n{totalWater}'
        if totalWater > maxWater:
            maxWater = totalWater
    
    return f'SAFE\n{maxWater}'

        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        maxWaterVolume = 0
        with open(fileName, 'r') as file:
            for i, line in enumerate(file):
                modLine = line.strip('\n')
                if i == 0:
                    numberOfCracks = int(modLine)
                    # print(f'number of cracks: {modLine}')
                elif i == 1: # positive integer
                    maxWaterVolume = int(modLine)
                    # print(f'threshold for how much flooding the village can withstand: {modLine}')
                elif i == 2: # positive integer
                    villageDrain = int(modLine)
                    # print(f'the amount of water that will drain out of the village each time unit {modLine}')
                else:
                    myTuple = modLine.split(' ')
                    currentCrack = Crack(myTuple[0], myTuple[1])
                    if myTuple[0] not in myDict:
                        myList = []
                        myList.append(currentCrack)
                        myDict[myTuple[0]] = myList
                    else:
                        myList = myDict[myTuple[0]]
                        myList.append(currentCrack)
                    # print(currentCrack)
        myResult = village(maxWaterVolume, villageDrain)
        print(myResult)






