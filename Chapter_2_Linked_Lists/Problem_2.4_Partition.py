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

    def partition(self, node, value):
        head = node
        tail = node

        while node is not None:
            next_node = node.nextNode
            node.nextNode = None

            if node.data >= value:
                tail.nextNode = node
                tail = node
            else:
                node.nextNode = head
                head = node
            node = next_node
        return head


ll = LinkedList()

ll.addNode(3)
ll.addNode(5)
ll.addNode(8)
ll.addNode(5)
ll.addNode(10)
ll.addNode(2)
ll.addNode(1)


result = ll.partition(ll.head, 5)
print(result.data)
print(result.nextNode.data)
print(result.nextNode.nextNode.data)


