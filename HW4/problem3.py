import math

fileName = './testRightAngle/rightangles_2.txt'

# cleanSet = set()
myList = []


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i > 0:
            newLine = line.strip('\n')
            myList.append(newLine)

class position: 
    def __init__(self, str):

        list = str.split(' ')
        self.x = int(list[0])
        self.y = int(list[1])
    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self
    def __ne__(self, other):
        if self.y == other.y and self.x == other.x:
            return False
        return True
    def distance(self, other):
        xVal = self.x - other.x
        yVal = self.y - other.y

        x2 = pow(xVal, 2)
        y2 = pow(yVal, 2)

        val = x2 + y2
        d = math.sqrt(val)
        return d
    def distanceFromOrigin(self):

        x2 = pow(self.x, 2)
        y2 = pow(self.y, 2)

        val = x2 + y2
        d = math.sqrt(val)
        
    def slope(self):
        if self.x == 0:
            return 0
        return  self.y / self.x
    def slope2(self, other):
        xVal = self.x - other.x
        yVal = self.y - other.y
        if xVal == 0:
            return 0
        return yVal / xVal
    def print(self):
        print(self.x, self.y)

    def getPosition(self):
        pos = str(self.x)+ ' ' + str(self.y)
        return pos

# Define a node in the BST
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Define the BST
class BST:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:  # val >= node.val
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    # Search for a value in the BST
    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    # Inorder traversal (sorted order)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)



def uRightTriangle(list):
    # computes all unique right triangles
    count = 0

    oLength = len(list)

    for i in range(oLength):
        myList = []
        degList = []

        posOffset = position(list[i])
        for j in range(oLength):
            if j != i:
                tempPos = position(list[j])
                newPos = tempPos - posOffset
                if newPos.x == 0:
                    radians = math.pi / 2  # vertical line
                else:
                    radians = math.atan(newPos.y / newPos.x)

                degrees = math.degrees(radians)
                degList.append(degrees)
        print(degList)
        newLen = len(degList)
        # print(newLen)
        for i in range(newLen):
            let = newLen - i - 1
            if i == newLen - 1:
                break
            for j in range(let):
                diff = degList[i] - degList[j + i + 1]
                if abs(diff - 90) < 1e-6 or abs(diff + 90) < 1e-6:
                    count += 1
    return count


result = uRightTriangle(myList)
print(result)