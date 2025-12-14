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
    
def villageGame(threshold, drain): # trash
    totalWater = 0
    maxWater = 0
    waterFlow = 0
    previousKey = None
    myHeap = MaxHeap()
    for key in myDict:
        myList = myDict[key]
        if previousKey != None:
            
            diff = int(key) - int(previousKey) - 1
            for i in range(diff):
                isEmpty = myHeap.is_empty()
                if not isEmpty:
                    myHeap.step(1)
                    waterFlow += myHeap.size()

                    topVal = myHeap.pop()
                    waterFlow -= topVal
                    print(f'waterFlow: {waterFlow}')
                    print(myHeap._heap)
                    totalWater += waterFlow - drain
                    # print(f'totalWater: {totalWater}')
                    if totalWater > maxWater:
                        maxWater = totalWater
                    if totalWater >= threshold:
                        return ('FLOOD')
                else:
                    totalDrain = drain * (diff - i)
                    totalWater -= totalDrain
                    if totalWater < 0:
                        totalWater = 0
                    break
            myHeap.step(1)
            waterFlow += myHeap.size()
        for e in myList:
            waterFlow += int(e.crackSize)
            myHeap.push(int(e.crackSize))
        # water = sum of the nodes + size of the list - top value in heap
        topVal = myHeap.pop()
        waterFlow -= topVal
        totalWater += waterFlow
        totalWater -= drain

        if totalWater > maxWater:
            maxWater = totalWater
        if totalWater >= threshold:
            return ('FLOOD')
        previousKey = key
        print(f'totalWater: {totalWater} waterFlow: {waterFlow}')
        print(myHeap._heap)
    
    length = myHeap.size()
    for i in range(length):
        topVal = myHeap.pop()
        waterFlow -= topVal
        totalWater += waterFlow
        totalWater -= drain
        if totalWater > maxWater:
            maxWater = totalWater
        if totalWater >= threshold:
            return ('FLOOD')
        
    return ('SAFE', maxWater)

              

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

        count = 0
        maxVal = 0
        totalWaterVolume = 0
        currentWaterVolume = 0
        result = 'SAFE'
        myMaxHeap = MaxHeap()
        
        while not myMaxHeap.is_empty() or numberOfCracks > 0:
            myStr = str(count)
            # print(f'count: {count}, cracks: {numberOfCracks}, empty: {myMaxHeap.is_empty()}')
            timeOffset = 0
            # If there are numbers then I can pop
            if myStr in myDict:
                myList = myDict[myStr]
                length = len(myList)
                numberOfCracks -= length
                # print(f'numberOfCracks: {numberOfCracks}')
                # print(f'Added: {myList}')
                for i in range(length):
                    currentCrack = myList[i]
                    currentSize = int(currentCrack.crackSize)
                    currentWaterVolume += currentSize
                    myMaxHeap.push(currentSize)
                crackFixed = myMaxHeap.pop()
                currentWaterVolume -= crackFixed
                timeOffset = myMaxHeap.size()
            else:
                emptyHeap = myMaxHeap.is_empty()
                if not emptyHeap:
                    # print('HEAP IS NOT EMPTY')
                    crackFixed = myMaxHeap.pop()
                    currentWaterVolume -= crackFixed
                    timeOffset = myMaxHeap.size()
    

            totalWaterVolume += currentWaterVolume - villageDrain
         
            if totalWaterVolume < 0:
                totalWaterVolume = 0
            
            if totalWaterVolume > maxVal:
                maxVal = totalWaterVolume
            
            myMaxHeap.step(1)
            
            if totalWaterVolume >= maxWaterVolume:
                # print(f'time: {count}')
                result = 'FLOOD'
                break
            
            if myMaxHeap.is_empty() and numberOfCracks < 1:
                break
                
          
            currentWaterVolume += timeOffset
            count += 1
     
        if result == 'FLOOD':
            print(result)
            print(count)
            print(totalWaterVolume)
        else:
            print(result)
            print(maxVal)
