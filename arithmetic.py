#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:57:08 2025

@author: duaijalshammari
"""

# A computing class that can calculate addition, subtraction, multiplication, and division

class Arithmetic:
    """ Provides addition and subtraction multiplication and division operations """
    
    def __init__(self):
        pass   # Initialization method, which can be extended to store historical calculation data and other functions
    
# Define add function to calculate addition.

    def add(self,a,b):
        return a + b 
# Define subtraction function to calculate subtraction.

    def subtract(self,a,b):
        return a - b
    
# Define multiply function to calculate multiplication.

    def multiply(self,a,b):
        return a * b
    
# Define divide function to calculate division.

    def divide(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        return a / b