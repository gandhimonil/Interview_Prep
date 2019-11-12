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

def delete_middle_node(node):
    if(node == None and node.nextNode == None):
        return False

    node.data = node.nextNode.data
    node.nextNode = node.nextNode.nextNode
    return True



node = Node(1)
node.nextNode = Node(2)
node.nextNode.nextNode = Node(3)
node.nextNode.nextNode.nextNode = Node(4)
node.nextNode.nextNode.nextNode.nextNode = Node(5)

to_delete = node.nextNode.nextNode.nextNode

print(delete_middle_node(to_delete))
