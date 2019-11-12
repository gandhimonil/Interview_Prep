class MinStack:

    def __init__(self):
        self.items = []
        self.stack_min = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

        # return self.items == []

    def push(self, item):
        self.items.append(item)

        if len(self.stack_min) == 0:
            self.stack_min.append(item)
        else:
            element = self.stack_min[len(self.stack_min) - 1]
            if item < element:
                self.stack_min.append(item)
            return element

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')

        element = self.items.pop()
        if element == self.stack_min.pop():
            self.stack_min.pop()
            return self.items.pop()
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    # def minimum(self, item):
    #     if len(self.stack_min) == 0:
    #         self.stack_min.append(item)
    #     else:
    #         element = self.stack_min.pop()
    #         if element < item:
    #             self.stack_min.append(item)
    #         return element

    def min(self):
        if len(self.stack_min) == 0:
            raise Exception('Stack is empty')
        else:
            return self.stack_min.pop()




s = MinStack()

print(s.isEmpty())
s.push(4)
s.push(7)
s.push(3)
print(s.peek())
print(s.size())
print(s.isEmpty())
s.push(8.4)
s.min()
s.min()
print(s.pop())
print(s.pop())
print(s.size())
