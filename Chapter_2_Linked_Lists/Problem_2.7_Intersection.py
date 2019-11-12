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

    def intersection(self, list1, list2):

        if list1 == None or list2 == None:
            return None

        list1_result = self.get_size_tail(list1)
        list2_result = self.get_size_tail(list2)

        if list1_result[0].data != list2_result[0].data:
            return False

        shorter = list1 if list1_result[1] < list2_result[1] else list2
        longer = list1 if list1_result[1] > list2_result[1] else list2

        # if longer == list1:
        #     diff = list1_result[1] - list2_result[1]
        # else:
        #     diff = list2_result[1] - list1_result[1]

        diff = abs(list1_result[1] - list2_result[1])

        current = longer.head

        for i in range(diff):
            current = current.nextNode

        current_shorter = shorter.head
        while current_shorter.data != current.data:
            current_shorter = current_shorter.nextNode
            current = current.nextNode

        return current.data


    def get_size_tail(self, list):

        current = list.head
        count = 1

        while current.nextNode:
            count += 1
            current = current.nextNode

        return [current, count]



ll = LinkedList()

ll.addNode(1)
ll.addNode(2)
ll.addNode(7)
ll.addNode(9)
ll.addNode(5)
ll.addNode(1)
ll.addNode(3)


# ll.printNode()

ll1 = LinkedList()

ll1.addNode(1)
ll1.addNode(2)
ll1.addNode(7)
ll1.addNode(6)
ll1.addNode(4)

# ll1.printNode()

print(ll.intersection(ll, ll1))