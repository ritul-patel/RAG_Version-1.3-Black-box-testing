import math
import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def safe_divide(a, b):
    """Safely divide a by b."""
    if b == 0:
        logging.error("Division by zero attempted")
        return None
    return a / b

def circle_area(radius):
    """Compute area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

class Calculator:
    """Simple calculator class."""

    def __init__(self):
        self.history = []

    def calculate_and_log(self, a, b, op):
        if op == "add":
            result = add(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = safe_divide(a, b)
        else:
            logging.warning("Unknown operation")
            return None

        self.history.append((op, a, b, result))
        return result
