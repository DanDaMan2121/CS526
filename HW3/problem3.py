# Using Recursion
# • Write a function that reverses a stack implemented as an array
# • Write a function that reverses a stack implemented as a Linked-list
# • Write a function that reverses a stack implemented as a doubly linked-list
# • Input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# • Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


# 3a -----

class myStackArray:
    def __init__(self):
        self.t = 0
        self.sSize = 0
        self.array = list()
    
    def size(self):
        return self.sSize
    
    def isEmpty(self):
        if self.sSize == 0:
            return True
        return False
    
    def push(self, e):
        self.array.append(e)
        if self.sSize != 0:
            self.t += 1
        self.sSize += 1

    def pop(self):
        if not self.isEmpty():
            poppedElement = self.array[self.t]
            self.array.pop(self.t)
            if self.t != 0:
                self.t -= 1
            self.sSize -= 1
            return poppedElement
        return None 
    
    def top(self):
        if self.isEmpty() != True:
            return self.array[self.t]
    def printStack(self):
        for e in self.array:
            print(e)


def reverseArray(stack):
    if stack.isEmpty():
        return
    top_element = stack.pop()
    reverseArray(stack)
    insertBottomArray(stack, top_element)

def insertBottomArray(stack, item):
    if stack.isEmpty():
        stack.push(item)
    else:
        top = stack.pop()
        insertBottomArray(stack, item)
        stack.push(top)

# aStack = myStackArray()

# aStack.push(5)
# aStack.push(15)
# aStack.push(25)

# print('Before: ')
# aStack.printStack()
# reverseArray(aStack)
# print('After: ')
# aStack.printStack()
# print()

# bStack = myStackArray()

# bStack.push(1)
# bStack.push(3)
# bStack.push(5)
# bStack.push(7)
# bStack.push(9)

# print('Before: ')
# bStack.printStack()
# reverseArray(aStack)
# print('After: ')
# bStack.printStack()
# print()

# cStack = myStackArray()

# cStack.push(1)
# cStack.push(23)
# cStack.push(456)
# cStack.push(7891)
# cStack.push(112)
# cStack.push(13)
# cStack.push(3)

# print('Before: ')
# cStack.printStack()
# reverseArray(aStack)
# print('After: ')
# cStack.printStack()
# print()


# 3b -----

class singleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
          


class myStackLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lSize = 0
    def size(self):
        return self.lSize
    
    def isEmpty(self):
        if self.lSize == 0:
            return True
        return False
    
    def push(self, e):
        newNode = singleLinkedNode(e)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif self.tail == self.head:
            newNode.next = self.tail
            self.head = newNode
            
        else:
            newNode.next = self.head
            self.head = newNode
        self.lSize += 1
        

    def pop(self):
        if self.isEmpty() == False:
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                newHead = self.head.next
                self.head = None
                self.head = newHead
            self.lSize -= 1

    def top(self):
        if self.isEmpty != True:
            return self.head.value
    
    def printStack(self):
        tempHead = self.head
        while tempHead != None:
            print(tempHead.value)
            tempHead = tempHead.next


def insertBottom(stack, item):
    if stack.isEmpty():
        stack.push(item)
    else:
        temp = stack.top()
        stack.pop()
        insertBottom(stack, item)
        stack.push(temp)

def reverseLinkedList(stack):
    if not stack.isEmpty():
        temp = stack.top()
        stack.pop()
        reverseLinkedList(stack)
        insertBottom(stack, temp)
    

# ll = myStackLinkedList()

# ll.push(10)
# ll.push(20)
# ll.push(30)
# ll.push(40)
# ll.push(50)
# ll.push(60)

# print('Before Reverse:')
# ll.printStack()
# print('After Reverse:')
# reverseLinkedList(ll)
# ll.printStack()
# print()

# lll = myStackLinkedList()

# lll.push(1)
# lll.push(2)
# lll.push(3)
# lll.push(4)
# lll.push(5)
# lll.push(6)
# lll.push(7)


# print('Before Reverse:')
# lll.printStack()
# print('After Reverse:')
# reverseLinkedList(lll)
# lll.printStack()
# print()

# llll = myStackLinkedList()

# llll.push(429)
# llll.push(7212)
# llll.push(3111)

# print('Before Reverse:')
# llll.printStack()
# print('After Reverse:')
# reverseLinkedList(llll)
# llll.printStack()
# print()

# 3c -----

class doublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
          


class myStackDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dSize = 0
    def size(self):
        return self.dSize
    
    def isEmpty(self):
        if self.dSize == 0:
            return True
        return False
    
    def push(self, e):
        newNode = doublyLinkedNode(e)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif self.tail == self.head:
            newNode.next = self.tail
            self.tail.prev = newNode
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.dSize += 1
        

    def pop(self):
        if self.isEmpty() == False :
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                newHead = self.head.next
                newHead.prev = None
                self.head = None
                self.head = newHead
            self.dSize -= 1
    
    def top(self):
        if self.isEmpty() != True:
            return self.head.value
    def printStack(self):
        tempNode = self.head
        while tempNode != None:
            print(tempNode.value)
            tempNode = tempNode.next

dl = myStackDoublyLinkedList()  

dl.push(1)
dl.push(2)
dl.push(3)
dl.push(4)
dl.push(5)
dl.push(6)

print('Before Reverse:')
dl.printStack()
print('After Reverse:')
reverseLinkedList(dl)
dl.printStack()
print()


ddl = myStackDoublyLinkedList()

# Test case for ddl
ddl.push(10)
ddl.push(20)
ddl.push(30)
ddl.push(40)

print('Before Reverse (ddl):')
ddl.printStack()
reverseLinkedList(ddl)
print('After Reverse (ddl):')
ddl.printStack()
print()

dddl = myStackDoublyLinkedList()
dddl.push(100)
dddl.push(200)
dddl.push(300)

print('Before Reverse (dddl):')
dddl.printStack()
reverseLinkedList(dddl)
print('After Reverse (dddl):')
dddl.printStack()
print()




