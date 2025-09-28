import inspect
from temp_conversion_tool import main

def test_user_interaction():
    # Check if the main function exists
    assert 'main' in globals(), "Function main does not exist."

    # Check if it is a function
    assert inspect.isfunction(main), "main is not a function."

    # Check for user prompt in the main function
    with open('temp_conversion_tool.py', 'r') as file:
        content = file.read()

    assert "Is this temperature in Celsius or Fahrenheit? (C/F):" in content, 
        "User prompt for temperature unit is missing."

    print("All checks passed.")

if __name__ == "__main__":
    test_user_interaction()

