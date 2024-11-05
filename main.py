import random 
def roll_dice_simulation(): # Ask the user for the number of rolls

num_rolls = int(input("Enter the number of times to roll the dice: ")) # Initialize a list to count occurrences of each possible sum (from 2 to 12) 
roll_counts = [0] * 11 # Index 0 corresponds to sum 2, index 10 corresponds to sum 12 
# Simulate rolling the dice 
for _ in range(num_rolls): 
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6) 
    roll_sum = die1 + die2 
    roll_counts[roll_sum - 2] += 1 # Adjust to zero-based index for list 
# Display the results as a chart 
print("\nRoll Distribution:") 
for i in range(2, 13): # Sums from 2 to 12 
    print(f"Sum of {i}: {'*' * roll_counts[i - 2]}") # Run the simulation 

roll_dice_simulation()
