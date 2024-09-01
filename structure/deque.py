import numpy as np

class Deque:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__front = -1
        self.__last = 0
        self.__length = 0
        self.__deque = np.empty(self.__capacity, dtype=int)

    def __full_deque(self):
        return(self.__front == 0 and self.__last == self.__length - 1) or (self.__front == self.__last + 1)
    
    def __empty_deque(self):
        return self.__front == - 1
    
    def add_front(self, value):
        if self.__full_deque():
            print("Deque is full")
            return
        if self.__front == -1:
            self.__front = 0
            self.__last = 0
        elif self.__front == 0:
            self.__front = self.__capacity - 1
        else:
            self.__front -= 1

        self.__deque[self.__front] = value

    def add_last(self, value):
        if self.__full_deque():
            print("Deque is full")
            return
        if self.__front == -1:
            self.__front = 0
            self.__last = 0
        elif self.__last == self.__capacity - 1:
            self.__last = 0
        else:
            self.__last += 1

        self.__deque[self.__last] = value

    def remove_front(self):
        if self.__empty_deque():
            print("Deque is empty")
            return
        if self.__front == self.__last:
            self.__front = -1
            self.__last = -1
        else:
            if self.__front == self.__capacity - 1:
                self.__front = 0
            else:
                self.__front += 1

    def remove_last(self):
        if self.__empty_deque():
            print("Deque is empty")
            return
        if self.__front == self.__last:
            self.__front = -1
            self.__last = -1
        elif self.__front == 0:
            self.__last = self.__capacity - 1
        else:
            self.__last -= 1
            
    def get_front(self):
        if self.__empty_deque():
            print("Deque is empty")
            return
        return self.__deque[self.__front]
    
    def get_last(self):
        if self.__empty_deque():
            print("Deque is empty")
            return
        return self.__deque[self.__last]


# Test

# Create a new Deque

deque = Deque(5)

# Insert elements into the Deque

deque.add_front(3)
deque.add_front(5)
deque.add_last(1)

# Print the front element

print(deque.get_front())

# Print the last element

print(deque.get_last())

# Remove the front element

deque.remove_front()

# Print the front element

print(deque.get_front())

# Insert element at the end

deque.add_last(4)

# Print the last element

print(deque.get_last())