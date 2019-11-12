class Two_Stacks_One_Array:

    def __init__(self, size):  #n is the size of the stack
        self.size = size
        self.arr = [None] * size
        self.first_stack = -1                   #top stack starting from the left side of the array
        self.second_stack = self.size           #bottom stack starting from the right side of the array


#     Method to push element in first_stack
    def push_first_stack(self, element):

        if self.first_stack < self.second_stack - 1:
            self.first_stack += 1
            self.arr[self.first_stack] = element
        else:
            print("Stack Overflow")
            exit(1)


    def push_second_stack(self, element):

        if self.first_stack < self.second_stack - 1:
            self.second_stack -= 1
            self.arr[self.second_stack] = element
        else:
            print("Stack Overflow ")
            exit(1)

    def pop_first_stack(self):

        if self.first_stack >= 0:
            element = self.arr[self.first_stack]
            self.first_stack -= 1
            return element
        else:
            print("Stack UnderFlow")
            exit(1)

    def pop_second_stack(self):

        if self.second_stack < self.size:
            element = self.arr[self.second_stack]
            self.first_stack += 1
            return element
        else:
            print("Stack UnderFlow")
            exit(1)

    def print_stack(self):
        for element in self.arr:
            print(element)



stack = Two_Stacks_One_Array(8)

stack.push_first_stack(1)
stack.push_first_stack(2)
stack.push_first_stack(3)


stack.push_second_stack(6)
stack.push_second_stack(7)
stack.push_second_stack(8)

print(stack.pop_first_stack())
print(stack.pop_second_stack())

stack.print_stack()




