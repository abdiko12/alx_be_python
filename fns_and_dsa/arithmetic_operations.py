#first
"""
arithmetic_operations.py
Function: perform_operation
Parameters: num1, num2, operation
"""

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: Result of the operation, or an error message.
    """
    # Normalize the operation string
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
#end
