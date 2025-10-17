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
    # print(list)
    pos1 = position(list[0])
    offset1 = length - 1

    for j in range(offset1):
        currentVal = list[j + 1]
        pos2 = position(currentVal)
        distance1 = pos1.distance(pos2)
        a = pow(distance1, 2)
        offset2 = length - j - 2
        for i in range(offset2):
            print('run', i)
            pos3 = position(list[j + i + 2])
            distance2 = pos1.distance(pos3)
            b = pow(distance2, 2)
            distance3 = pos2.distance(pos3)
            c = pow(distance3, 2)
            # print(distance1, distance2, distance3)
            print('distance1:', distance1, ' distance2:', distance2, ' distance 3:', distance3)
            if a != 0 and b != 0 and c != 0:
                if a == (b + c):
                    ans += 1
                    print('ding')
                elif b == (a + c):
                    ans += 1
                    print('ding')
                elif c == (a + b):
                    ans += 1
                    print('ding')
                print(pos1.getPosition(), pos2.getPosition(), pos3.getPosition())
    
                
    
    avoidDupes(list[1:], ans)

ans = 0
ans = avoidDupes(myList, ans)
print(ans)