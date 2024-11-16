import random

def int_check(value):
    while not value.isdigit() or int(value) <= 0:
        value = input("Please enter a positive number: ")
    return int(value)
    
# Ask the user for the number of rolls
def roll_dice_simulation():
    print('In this program, you would enter a number above 0 and it would randomly roll 2 dies based on your input.')
    num_rolls = input("Enter the number of times to roll the dice: ") 
    num_rolls = int_check(num_rolls)
    # Initialize a list to count occurrences of each possible sum (from 2 to 12) 
    roll_counts = [0] * 11 


    # Simulate rolling the dice
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        # Adjust to a zero-based index for the list
        roll_counts[roll_sum - 2] += 1

    # Display the results as a chart
    print("\nNumbers rolled:")
    # Sums from 2 to 12
    for i in range(2, 13):
        print(f"Sum of {i}: {'*' * roll_counts[i - 2]}")

    # Run the simulation


roll_dice_simulation()
print ('Thank you for using this dice simulator app')
