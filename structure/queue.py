import numpy as np

class Queue:
    
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__first = 0
        self.__last = -1
        self.__length = 0
        self.__queue = np.empty(self.__capacity, dtype=int)

    def __full_queue(self):
        return self.__length == self.__capacity        
    def __empty_queue(self):
        return self.__length == 0

    def enqueue(self, value):
        if self.__full_queue():
            print("Queue is full")
            return
        
        if self.__last == self.__capacity - 1:
            self.__last = -1
        self.__last += 1

        self.__queue[self.__last] = value
        self.__length += 1

    def dequeue(self):
        if self.__empty_queue():
            print("Queue is empty")
            return
        
        #temp = self.__queue[self.__first]
        self.__first += 1
        if self.__first == self.__capacity -1:
            self.__first = 0
        self.__length -= 1
        #return temp            

    def peek(self):
        if self.__empty_queue():
            return -1
        return self.__queue[self.__first]

        
# Test

# Create a new queue

queue = Queue(5)

# Insert elements into the queue

queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(1)

# Print the top element

print(queue.peek())

# Remove the top element

queue.dequeue()

# Print the top element

print(queue.peek())

# Insert element at the top

queue.enqueue(9)

# Print the top element

print(queue.peek())