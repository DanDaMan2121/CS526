# Problem 4
# Write a function to find the sum of the three middle nodes in a doubly linked list
# of sorted integers. You may assume the the list has an odd length

class Node:
    def __init__(self, next=None, prev=None, value=None):
        self.next = next
        self.prev = prev
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        newNode = Node(next=None, prev=self.tail, value=value)

        if newNode.next == None and newNode.prev == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail.value = None
            self.tail = None
        else:
            self.tail.value = None
            # The new tail is now the previous node of the current tail node
            newTail = self.tail.prev
            newTail.next = None
            # Remove the data from the old tail
            self.tail.prev = None
            self.tail.value = None
            # Set the new tail value
            self.tail = newTail
    
    def printList(self):
        if self.head == self.tail and self.head != None:
            print(self.head.value)
        else:
            tempNode = self.head
            while tempNode != None:
                print(tempNode.value)
                tempNode = tempNode.next

DLL = DoublyLinkedList()

DLL.push(2)
DLL.push(4)
DLL.push(8)
DLL.push(10)
DLL.push(15)
DLL.push(29)
DLL.push(41)



def printSumOfMiddle3(DLL):

    tempHead = DLL.head
    tempTail = DLL.tail

    while tempHead != tempTail:
        tempHead = tempHead.next
        tempTail = tempTail.prev

    sum = tempHead.value + tempHead.next.value + tempHead.prev.value
    print(sum)


printSumOfMiddle3(DLL)


# DLL2 = DoublyLinkedList()
# DLL2.push(10)
# DLL2.push(30)
# DLL2.push(50)

# printSumOfMiddle3(DLL2)