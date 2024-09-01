import numpy as np

class PriorityQueue:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__length = 0
        self.__priority_queue = np.empty(self.__capacity, dtype=int)

    def __full_queue(self):
        return self.__length == self.__capacity        
    
    def __empty_queue(self):
        return self.__length == 0
    
    def enqueue(self, value):
        if self.__full_queue():
            print("PriorityQueue is full")
            return
        
        if self.__length == 0:
            self.__priority_queue[self.__length] = value
            self.__length += 1
        else:
            x = self.__length - 1
            while x >= 0:
                if value > self.__priority_queue[x]:
                    self.__priority_queue[x + 1] = self.__priority_queue[x]
                else:
                    break
                x -= 1
            self.__priority_queue[x + 1] = value
            self.__length += 1
        
    
    def dequeue(self):
        if self.__empty_queue():
            print("PriorityQueue is empty")
            return
        
        value = self.__priority_queue[self.__length - 1]
        self.__length -= 1

    def peek(self):
        if self.__empty_queue():
            return -1
        return self.__priority_queue[self.__length - 1]
    
# Test

# Create a new priority queue

priority_queue = PriorityQueue(5)

# Insert elements into the priority queue

priority_queue.enqueue(3)
priority_queue.enqueue(5)
priority_queue.enqueue(1)

# Print the top element

print(priority_queue.peek())

# Remove the top element

priority_queue.dequeue()

# Print the top element

print(priority_queue.peek())