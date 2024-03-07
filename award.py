# Enter the users qualifying time for each event
print("Please note overall qualifying time for awards will be 110 mins and less")
print("Note negative numbers and characters will not be accepted")
print()

# Function to get valid time input from user
def get_valid_time(prompt):
        """
    Prompt the user to enter a positive integer for the time.
    
    Args:
    - prompt (str): The prompt message to display.
    
    Returns:
    - int: The positive integer entered by the user.
    """
    while True:
        try:
            time = int(input(prompt))
            if time < 0:
                raise ValueError("Negative time is not allowed")
            return time
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

# Get the finishing times for each event from the user
running = get_valid_time("Enter your finished running time in minutes: ")
swimming = get_valid_time("Enter your finished swimming time in minutes: ")
cycling = get_valid_time("Enter your finished cycling time in minutes: ")

# Calculate the total time to complete the triathlon
qual_time = running + swimming + cycling
print("Total time to complete triathlon:", qual_time, "minutes")
print()

# Determine the award based on the qualifying time
if qual_time < 101 and qual_time > 0:  # Award time will be equal to and between 0mins & 100mins
    print("You have been awarded Provincial Colours")
elif qual_time < 106 and qual_time > 100:  # Award time will be equal to and between 101mins & 105mins
    print("You have been awarded Provincial Half Colours")
elif 106 <= qual_time <= 110:  # Award time will be equal to and between 105mins & 110mins
    print("You have been awarded Provincial Scroll")
else:
    print("You receive no award")
