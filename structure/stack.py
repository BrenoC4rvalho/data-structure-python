import numpy as np

class Stack:
    
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__stack = np.empty(self.__capacity, dtype=int)

    def __full_stack(self):
        if self.__capacity - 1 == self.__top:
            return True
        else:
            return False
        
    def __empty_stack(self):
        if self.__top == -1:
            return True
        else:
            return False
        
    def stack_up(self, value):
        if self.__full_stack():
            print("Stack is full")
            return
        else:
            self.__top += 1
            self.__stack[self.__top] = value

    def unstack(self):
        if self.__empty_stack():
            print("Stack is empty")
            return
        else:
            self.__top -= 1

    def peek(self):
        if self.__empty_stack():
            return - 1
        else:
            return self.__stack[self.__top]
        
# Test

# Create a new Stack

stack = Stack(5)

# Insert elements into the stack

stack.stack_up(3)
stack.stack_up(5)
stack.stack_up(1)

# Print the top element

print(stack.peek())

# Remove the top element

stack.unstack()

# Print the top element

print(stack.peek())

# Insert element at the top

stack.stack_up(9)

# Print the top element

print(stack.peek())