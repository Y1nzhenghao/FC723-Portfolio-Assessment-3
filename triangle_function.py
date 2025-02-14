
import math

class Trigonometry:
    """ Provides trigonometric function calculation """
    
    def __init__(self):
        pass   # Initialization method, which can be extended to store historical calculation data and other functions
    
# Define a function called sine to calculate the sine of a number.

    def sine(self,x):
        """ Calculate the sine value """
        radians = math.radians(x)   # Convert angles to radians.
        result = math.sin(radians)   # Calculate the sin value.
        return result   # Return to the result.
    
    def cosine(self,x):
        """ Calculate the cosine value """
        radians = math.radians(x)   # Convert angles to radians.
        result = math.cos(radians)   # Calculate the cosine value.
        return result   # Return to the result.
    
    def tangent(self,x):
        """ Calculate the tangent value """
        radians = math.radians(x)   # Convert angles to radians.
        result = math.tan(radians)   # Calculate the tangent value.
        return result   # Return to the result.
    
    def arcsine(self,x):
        """ Calculate arcsine value (Angle system) Since the range (output range) of sin(θ) is [-1,1], arcsin(x) can only accept input between -1 ≤ x ≤ 1.
        If the input is outside this range, there is no corresponding Angle, so an error message is returned."""
        if -1 <= x <= 1:
            radians = math.asin(x)   # Calculate arcsine radians.
            degrees = math.degrees(radians)   # Convert to Angle.
            return degrees
        return "Error: Input out of range"
    
    def arccosine(self,x):
        """ Calculate the inverse cosine (in Angle system) """
        if -1 <= x <= 1:   # Make sure the input is in the [-1, 1] range.
            radians = math.acos(x)   # Calculate arccosine radians.
            degrees = math.degrees(radians)   # Convert to Angle.
            return degrees
        return "Error: Input out of range"
    
    def arctangent(self,x):
        """ Calculate the inverse tangent """
        radians = math.atan(x)   # Calculate arctangent radians.
        degrees = math.degrees(radians)   # Convert to Angle.
        return degrees