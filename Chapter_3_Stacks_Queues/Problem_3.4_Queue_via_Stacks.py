class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):

        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


q = Queue()
q.enqueue(5)
q.enqueue(11)
q.enqueue(9)

print(q.dequeue())

q.enqueue(4)

q.dequeue()



