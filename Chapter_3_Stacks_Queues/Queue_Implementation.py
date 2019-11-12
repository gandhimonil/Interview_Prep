# ADT - Abstract Data Type Queue Implementation using Lists in Python pushing elements
# at the end and poping them from the end
class Queue_Implementation:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

        # return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Test_Queue:
    q = Queue_Implementation()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.dequeue())
    #print(q.size())
