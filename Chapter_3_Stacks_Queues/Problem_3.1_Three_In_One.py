# Three stacks in one array solution but with fixed sizes stacks
class MultiStack:

    def __init__(self, stacksize):
        self.stacknum = 3
        self.stacksize = stacksize
        self.arr = [0] * (stacksize * self.stacknum)
        self.sizes = [0] * self.stacknum

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.arr[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        element_return = self.arr[self.IndexOfTop(stacknum)]
        self.arr[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return element_return

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.arr[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0


    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize


    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1



newstack = MultiStack(8)

newstack.Push(3, 1)
newstack.Push(4,0)
newstack.Push(3,1)
newstack.Push(5,2)
newstack.Push(10,1)
newstack.Push(8,1)
newstack.Push(6,2)
newstack.Push(9,1)

print(newstack.Peek(1))
print(newstack.IsEmpty(1))
newstack.Push(2, 1)
print(newstack.Peek(1))
print(newstack.Pop(1))
print(newstack.Peek(1))
newstack.Push(3, 1)

