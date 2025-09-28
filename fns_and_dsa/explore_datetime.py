"""
explore_datetime.py

Demonstrates how to:
1. Display the current date and time.
2. Calculate a future date after adding a user-specified number of days.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtain and display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    Also saves the current date into a variable named current_date.
    """
    current_date = datetime.now()  # save current datetime
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # return for use in other functions if needed

def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date by adding days_to_add to current_date.
    Saves the result in a variable named future_date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    # Print in "YYYY-MM-DD" format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt user for days and calculate future date
    while True:
        try:
            days_str = input("Enter the number of days to add to the current date: ").strip()
            days_to_add = int(days_str)
            break
        except ValueError:
            print("Please enter a valid integer for the number of days.")

    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()
