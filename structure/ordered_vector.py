import numpy as np

class OrderVector:
    
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__last_index = -1
        self.__vector = np.empty(self.__capacity, dtype=int)

    def push(self, value):
        if self.__last_index == self.__capacity - 1:
            print("OrderVector is full")
        
        index = 0
        for i in range(self.__last_index + 1):
            index = i
            
            if self.__vector[i] > value:
                break
            
            if i == self.__last_index:
                index = i + 1
        

        x = self.__last_index 
        while self.__last_index >= index:
            self.__vector[x + 1] = self.__vector[x]
            x -= 1

        self.__vector[index] = value
        self.__last_index += 1

    def binary_search(self, value):
        lower_limit = 0
        upper_limit = self.__last_index

        while True:
            mid = int((lower_limit + upper_limit) / 2)
            
            if self.__vector[mid] == value:
                return mid
            elif lower_limit > upper_limit:
                return -1
            else:
                if self.__vector[mid] < value:
                    lower_limit = mid + 1
                else:
                    upper_limit = mid - 1

    def pop(self, value):
        index = self.binary_search(value)
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

vector = OrderVector(5)

# Insert elements into the vector

vector.push(3)
vector.push(5)
vector.push(1)
vector.push(4)
vector.push(2)

# Print the vector
print(vector)

# Search element
vector.binary_search(4)

# Remove element
vector.pop(4)

# Print the vector
print(vector)

# Insert element at the beginning
vector.push(0)
