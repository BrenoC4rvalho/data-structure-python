import numpy as np

class UnorderVector:
    
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__last_index = -1
        self.__vector = np.empty(self.__capacity, dtype=int)

    def push(self, value):
        if self.__last_index == self.__capacity:
            print("UnorderVector is full")
        else:
            self.__last_index += 1
            self.__vector[self.__last_index] = value

    def linear_search(self, value):
        for i in range(self.__last_index + 1):
            if self.__vector[i] == value:
                return i
            return -1

    def pop(self, value):
        index = self.linear_search(value)
        if index == -1:
            print(f"{value} not found in OrderVector")
        else:
            for i in range(index, self.__last_index):
                self.__vector[i] = self.__vector[i + 1]
            self.__last_index -= 1        

    def __str__(self):
        return str(self.__vector[:self.__last_index + 1])
    


# Test

# Create a new vector

vector = UnorderVector(5)

# Insert elements into the vector

vector.push(3)
vector.push(5)
vector.push(1)
vector.push(4)
vector.push(2)

# Print the vector
print(vector)

# Search element
vector.linear_search(4)

# Remove element
vector.pop(4)

# Print the vector
print(vector)

# Insert element at the beginning
vector.push(1)
