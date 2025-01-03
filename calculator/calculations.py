# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.
    
    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float): A number representing the first addend in addition.
        b (float): A number representing the second addend in addition.
        
    Returns:
        float: A number representing the arithmetic sum of 'a' and 'b'.
    """
    return float(a + b)
def subtract(a, b):
    """Compute and return the difference of two numbers.
    
    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0
        >>> subtract(-1, 3)
        -4.0

    Args:
        a (float): A number representing the first addend in subtraction.
        b (float): A number representing the second addend in subtraction.
        
    Returns:
        float: A number representing the arithmetic difference of 'a' and 'b'.
    """
    return float(a - b)
def multiply(a, b):
    """Compute and return the product of two numbers.
    
    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0
        >>> multiply(-1, 3)
        -3.0

    Args:
        a (float): A number representing the first addend in multiplication.
        b (float): A number representing the second addend in multiplication.
        
    Returns:
        float: A number representing the arithmetic product of 'a' and 'b'.
    """
    return float(a * b)
def divide(a, b):
    """Compute and return the division of two numbers.
    
    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(22, 4)
        5.5
        >>> divide(22, 7)
        3.142857142857143

    Args:
        a (float): A number representing the first addend in division.
        b (float): A number representing the second addend in division.
        
    Returns:
        float: A number representing the arithmetic division of 'a' and 'b'.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a/b)