#fourth project

# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
#end
