import math

fileName = './testRightAngle/righttangles_1.txt'

cleanSet = set()


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i != 0:
            newLine = line.strip('\n')
            cleanSet.add(newLine)
# cleanSet.add('0 4')

# print(cleanSet)
myList = list(cleanSet)

class position: 
    def __init__(self, string):
        self.x = int(string[0])
        self.y = int(string[2])
    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self
    def distance(self, other):
        xVal = pow((self.x - other.x), 2)
        yVal = pow((self.y - other.y), 2)
        d = math.sqrt(yVal + xVal)
        return d
    
    def slope(self, other):
        xVal = self.x - other.x
        yVal = self.y - other.y
        return  yVal / xVal
    def print(self):
        print(self.x, self.y)

    def getPosition(self):
        pos = str(self.x)+ ' ' + str(self.y)
        return pos

def avoidDupes(list, ans):
    length = len(list)
    # print(ans)
    print(list)
    if length < 3:
        print(ans)
        return ans
    offset = position(list[0])
    llenght = length - 1

    for i in range(llenght):
        currentPos = position(list[i + 1])
        currentPos = currentPos - offset
        distance = currentPos.distance(offset)
        print(distance)

        angleInRadian = math.atan(distance)
        angleInDegrees = math.degrees(angleInRadian)
        # print(angleInDegrees)
        # currentPos.print()

    
    avoidDupes(list[1:], ans)

ans = 0
ans = avoidDupes(myList, ans)
print(ans)