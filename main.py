import random


# Ask the user for the number of rolls
def roll_dice_simulation():
    while True:
        try:
            num_rolls = int(input("Enter the number of times to roll the dice: "))
            if num_rolls > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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