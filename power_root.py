import math

class PowerRoot:
    """ Provides square and square root calculation function """
    
    def __init__(self):
        pass   # Initialization method, which can be extended to store historical calculation data and other functions
    
# Define a function called squared to compute the square of a number.

    def square(self, x):
        return x ** 2
    
# Define a function called suqare root to calculate the square root of a number.

    def square_root(self,x):
        if x < 0:
            return "Numbers less than 0 cannot be calculated as square roots."
        return math.sqrt(x)