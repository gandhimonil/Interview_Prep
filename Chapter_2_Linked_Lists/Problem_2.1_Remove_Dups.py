
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


def delete_duplicates(n):

    # if n.head == None:
    #     return
    #
    # previous = n.head
    # current = previous.nextNode
    #
    # set_buffer = set()
    # set_buffer.add(previous.data)
    #                                                           Solution 1 - with set acting as a buffer
    # while previous.nextNode != None:
    #
    #     if current.data in set_buffer:
    #         previous.nextNode = current.nextNode
    #         current = current.nextNode
    #     else:
    #
    #         set_buffer.add(current.data)
    #         previous = current
    #         current = current.nextNode
    #

    if n.head == None:
        return

    current = n.head

    while current != None:
        running_pointer = current
        while running_pointer.nextNode != None:
            if running_pointer.nextNode.data == current.data:
                running_pointer.nextNode = running_pointer.nextNode.nextNode            # Solution with pointers but no buffer
            else:
                running_pointer = running_pointer.nextNode
        current = current.nextNode


ll = LinkedList()

ll.addNode(2)
ll.addNode(3)
ll.addNode(1)
ll.addNode(2)
ll.addNode(1)
ll.addNode(4)
# ll.printNode()

delete_duplicates(ll)
ll.printNode()
