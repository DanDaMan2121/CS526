# Problem 2
# Consider the following function 
# def doIt(node)
#     if node is None :
#         return
#     doIt(node.next)
#     print(node.value)


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



def doIt(node):
        if node is None :
            return
        doIt(node.next)
        print(node.value)

DLL = DoublyLinkedList()

DLL.push(12)
DLL.push(3)
DLL.push(5)
DLL.push(2)

doIt(DLL.head)
# The function doIt prints the linked listed in reverse order