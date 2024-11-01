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

# Purpose: Display all the roll sums
# Name: display_results
# Parameters: sum_counter(list of numbers)
# Return: None
# Algorithm
# 1. Loop through the sum_counter list using index with 0 to 10
# 2. for every index, put "Sum of (the sum number)"

# Purpose: Main function to use everything 
# Name: Main
# Parameters: None
# Return: None
# Algorithm
# 1. call get_num_rolls to get the users ammount of rolls they want.
# 2. Call roll_dice using the number of rolls to get the sum counter.
# 3. call display_results with the sum counter to display all the sums of the dice
# 4. print ending messege "thank you for using this application"

