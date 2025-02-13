# def getslope(m, x, b):
#     return m * x + b

# def test_getslope():
#     assert getslope(2,2,1) == 5

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers, handles division by zero."""
    return a / b if b != 0 else "Cannot divide by zero"

def power(base, exponent):
    """Returns the result of raising base to the power of exponent."""
    return base ** exponent

def modulus(a, b):
    """Returns the remainder when a is divided by b."""
    return a % b

def average(*numbers):
    """Returns the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

functionstorage = [
    add(1,4), subtract(8,3), multiply(2,4), divide(60,12), power(-), modulus(), average(), 
]

def tester():
    for function in functionstorage:
        assert function == 5