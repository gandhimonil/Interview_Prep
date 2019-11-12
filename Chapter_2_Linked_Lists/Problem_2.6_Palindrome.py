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


    def is_palindrome(self, ll):

        fast = ll.head
        slow = ll.head
        stack = []

        while fast and fast.nextNode:
            stack.append(slow.data)
            slow = slow.nextNode
            fast = fast.nextNode.nextNode

        if fast:
            slow = slow.nextNode

        while slow:
            value = stack.pop()

            if slow.data != value:
                return False

            slow = slow.nextNode


        return True











ll = LinkedList()

ll.addNode(0)
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(0)


print(ll.is_palindrome(ll))


