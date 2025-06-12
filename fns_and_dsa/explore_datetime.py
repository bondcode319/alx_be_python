from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculates and displays a future date based on user input.
    """
    try:
        # Prompt user for number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Get current date
        current_date = datetime.now()
        
        # Calculate future date by adding the specified number of days
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

def main():
    """
    Main function to execute the datetime exploration tasks.
    """
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()