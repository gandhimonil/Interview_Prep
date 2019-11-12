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

    def sum_lists(self, num1, num2):
        ll_head = num1.head
        ll1_head = num2.head

        ll_return = LinkedList()

        carry = 0

        while ll_head and ll1_head:
            result = carry

            if ll_head:
                result += ll_head.data
                ll_head = ll_head.nextNode
            if ll1_head:
                result += ll1_head.data
                ll1_head = ll1_head.nextNode

            ll_return.addNode(result % 10)
            carry = result // 10


        if carry:
            ll_return.addNode(carry)

        return ll_return


ll = LinkedList()

ll.addNode(2)
ll.addNode(1)
ll.addNode(5)

# ll.printNode()

ll1 = LinkedList()

ll1.addNode(9)
ll1.addNode(1)
ll1.addNode(9)

# ll1.printNode()



result = ll.sum_lists(ll, ll1)

result.printNode()



