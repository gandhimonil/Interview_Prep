# ADT - Abstract Data Type Stack Implementation using Lists in Python pushing elements
# at the end and poping them from the end
class Stack_Implementation:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

        # return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_elements(self,stack):
        for i in range(len(stack)):
            print(stack[i])

    def array_return(self):
        return self.items

class sort_stack:


    # 1) Create a temporary stack say tmpStack.
    # 2) While input stack is NOT empty do this:
    #    --> Pop an element from input stack call it temp
    #    --> while temporary stack is NOT empty and top of temporary stack is greater than temp,
    #           pop from temporary stack and push it to the input stack
    #    --> push temp in temporary stack
    # 3) The sorted numbers are in tmpStack

    def sort_stack(self, stack):
        temp_stack = Stack_Implementation()

        while not stack.isEmpty():

            temp = stack.pop()

            while not temp_stack.isEmpty() and temp_stack.peek() > temp:
                stack.push(temp_stack.pop())

            temp_stack.push(temp)

        # while not temp_stack.isEmpty():
        #     stack.push(temp_stack.pop())

        return temp_stack




class Test_Stack:

    s = Stack_Implementation()

    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())

    s.push(34)
    s.push(3)
    s.push(31)
    s.push(98)
    s.push(92)
    s.push(23)

    s_init = sort_stack()
    result = s_init.sort_stack(s)

    # result.print_elements(result.array_return())










