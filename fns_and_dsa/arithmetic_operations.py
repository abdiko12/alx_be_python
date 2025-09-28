#first
"""
arithmetic_operations.py

Defines the perform_operation function for basic arithmetic operations.
"""

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters
    ----------
    num1 : float
        The first number.
    num2 : float
        The second number.
    operation : str
        One of: 'add', 'subtract', 'multiply', 'divide'.

    Returns
    -------
    float | str
        The result of the arithmetic operation, or a message if
        an invalid operation is provided or division by zero occurs.
    """
    operation = operation.lower().strip()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"  # Recognizable message for main.py
        return num1 / num2
    else:
        return "Error: Invalid operation"
#end
