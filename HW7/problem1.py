import sys
import heapq
myDict = dict()
myEncodeDict = dict()
myDecodeDict = dict()

def currentExpSort(myList, exp):
    n = len(myList)
    output = [0] * (n)
    occurrences = [0] * (10)
    
    for i in range(0, n):
        index = myDict[myList[i]] // exp
        occurrences[index % 10] += 1
    for i in range(1, 10): 
        occurrences[i] += occurrences[i - 1]
    

    i = n - 1
    while i >= 0:
        index = myDict[myList[i]] // exp 
        output[occurrences[index % 10] - 1] = myList[i]
        occurrences[index % 10] -= 1
        i -= 1
    # print(output)
    return output

def radixSort(myList):
    largestElement = myDict[myList[0]]

    for i in range(len(myList)):
        if myDict[myList[i]] > largestElement:
            largestElement = myDict[myList[i]]

    exp = 1
    while largestElement / exp >= 1:
        myList = currentExpSort(myList, exp)
        exp *= 10

    # print(myList)
    return myList

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.value, node))

    def pop(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0
    def sizeOf(self):
        return len(self.heap)

class Node:
    def __init__(self, value):
        self.char = None
        self.value = value
        self.code = ''
        self.left = None
        self.right = None
    def __repr__(self):
        if self.char != None:
            if self.char == '\n':
                return f"Node(\\n)"
            return f"Node({self.char})"
        return f"Node({self.value})"
    def __lt__(self, other):
        return self.value < other.value

class BST:
    def __init__(self):
        self.root = None

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            if node.left:
                node.left.code = node.code + '0'
            self._inorder(node.left, result)
            result.append(node)

            if node.right:
                node.right.code = node.code + '1'

            self._inorder(node.right, result)

def encodeMessage(mySentences):
    sLength = len(mySentences)
    myCode = ''
    for i in range(sLength):
        mySentence = mySentences[i]
        length = len(mySentence)
        for j in range(length):
            myCode += myEncodeDict[mySentence[j]]
    return myCode

def decodeMessage(message):
    mLength = len(message) + 1
    start = 0
    oMessage = ''
    for i in range(mLength):
        code = message[start: i]
        if code in myDecodeDict:
            oMessage += myDecodeDict[code]
            start = i
    
    return oMessage


if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]

        myList = []
        mySentences = []
        with open(fileName, 'r') as file:
            # PART 1
            # input set
            print('PART 1:')
            print('Input set:')

            for i, line in enumerate(file):
                print(line, end='')
                myChars = list(line)
                for char in myChars: # gives me the frequency of each character in the document / long string
                    if char in myDict:
                        myDict[char] += 1
                    else:
                        myDict[char] = 1
                mySentences.append(myChars)
            print()
            print('------')

        myList = list(myDict) # collects each distinct char
        sortedList = radixSort(myList) # modified radix sort to sort the list by the frequency of each character from smallest to largest

        myQueue = PriorityQueue()
        # pushes all chars to a priority queue smaller frequency higher priority
        for e in sortedList:
            newNode = Node(myDict[e])
            newNode.char = e
            myQueue.push(newNode)
        
        # Huffman coding
        while(myQueue.sizeOf() > 1):
            node1 = myQueue.pop()
            node2 = myQueue.pop()
            # print(f'Node1: {node1} Node2: {node2}')
            sum = node1.value + node2.value
            newNode = Node(sum)
            newNode.left = node1
            newNode.right = node2
            myQueue.push(newNode)
                
        myBST = BST()
        myBST.root = myQueue.peek()
        # generates tree, and the code of each character
        result = myBST.inorder()

    
        # generates frequency map
        print('Frequency Map:')
        for e in result:
            if e.char != None:
                myEncodeDict[e.char] = e.code
                myDecodeDict[e.code] = e.char
                if e.char == '\n':
                    print(f'CHAR: \\n FREQNEUNCY: {e.value} CODE: {e.code}')
                else:
                    print(f'CHAR: {e.char} FREQUENCY: {e.value} CODE: {e.code}')
        print('-----')

        # tree in order traversal
        print('Tree Inorder Traversal')
        print(result)
        print('-----')

        # compressed message
        myCode = encodeMessage(mySentences)
        print('Input compressed:')
        print(myCode)
        print('-----')

        # PART 2
        compressedFileName = './compressedFiles/'
        compressedFileName += input('Enter a fileName: ')
        print('-----')
        with open(compressedFileName, 'w') as file:
            file.write(myCode)
        
        with open(compressedFileName, 'r') as file:
            myEncodedMessage = file.read()

        print('PART2:')
        print(f'Input set:')
        print(myEncodedMessage)
        print('-----')
        
        print('Message decompressed:')
        originalMessage = decodeMessage(myEncodedMessage)
        print(originalMessage)
        print('-----')
        
        decompressedFileName = './decompressedFiles/'
        decompressedFileName += input('Enter a fileName: ')
        with open(decompressedFileName, 'w') as file:
            file.write(originalMessage)
        # print(f'Output set:\n{originalMessage}')

        

                