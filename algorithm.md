# Purpose: Prompt the user to enter the ammount of times they want to roll the dice
# Name: get_num_rolls
# Parameters: None
# Return: num_rolls, it will return a intiger that is the number of times the user wants to roll the dice.
# Algorithm: 
#    1. prompt the user to enter the number of rolls.
#    2. make sure that the number is posotive
#    3. Return the number of roles which will be called num_roles

# Purpose: Rolling the dice
# Name: roll_dice
# Parameters: num_roles
# Return: sum_counter, sum_counter is a list which has the count of all the sums
# Algorithm:
# 1. Create a list holding 11 numbers. 
# 2. Generate 2 random numbers between 1-6
# 3.add the two numbers 
# 4.keep repeating that for num_rolls ammount of times. 
# incrase the corresponding spot in sum_counter by 1 depending what the dice add up to
