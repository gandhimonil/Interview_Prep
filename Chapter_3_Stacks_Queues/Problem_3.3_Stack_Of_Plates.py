class MultiStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, item):
        # if len(self.stacks) == 0:
        #     new_stack = []
        #     new_stack.append(item)
        #     self.stacks.append(new_stack)
        # else:
        #     latest_stack = self.stacks.pop()
        #     if len(latest_stack) == self.capacity:            #Lengthly Code
        #         new_stack = []
        #         new_stack.append(item)
        #         self.stacks.append(new_stack)
        #     else:
        #         latest_stack.append(item)

        if len(self.stacks) and (len(self.stacks[-1]) < self.capacity):
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        if len(self.stacks) == 0:
            return None
        element = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return element

    def pop_at(self, stack_number):
        if stack_number < 0 and (stack_number >= len(self.stacks)):
            return None
        if len(self.stacks[stack_number]) == 0:
            return None
        return self.stacks[stack_number].pop()


stack = MultiStack(3)
stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)
stack.push(55)
stack.push(66)
stack.push(77)
stack.push(88)

stack.pop()
stack.pop()
stack.pop()

stack.pop_at(0)

stack.pop_at(2)