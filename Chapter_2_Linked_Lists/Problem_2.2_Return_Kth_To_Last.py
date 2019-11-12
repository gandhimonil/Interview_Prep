# Definition for singly-linked list.
class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return True

    def printNode(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nextNode

def nth_to_last(ll, k):

    pointer1 = ll.head
    pointer2 = ll.head


    for i in range(k):
        if pointer2 == None:
            return

        pointer2 = pointer2.nextNode

    while pointer2 != None:
        pointer2 = pointer2.nextNode
        pointer1 = pointer1.nextNode

    return pointer1.data

ll = LinkedList()

ll.addNode(2)
ll.addNode(3)
ll.addNode(1)
ll.addNode(2)
ll.addNode(1)
ll.addNode(4)

print(nth_to_last(ll, 2))

