# Purpose: Error input checking
# Name: int_check
# Parameters: value
# Return: num_rolls, number of rolls if it is a valid value
# Algorithm: 
#    1. while num_rolls is not a number.
#        A. prompt user to enter number of rolls again
#    2. while num_rolls is not positive
#        A. prompt user to enter number of rolls again
#    3. Return the number of rolls

# Purpose: 
# Name: Main
# Parameters: None
# Return: None
# Algorithm
# 1. prompt user to enter number of rolls they want to roll the dies
# 2. call the int_check function to see if user input is valid
# 3. create a list to store all the roll sums
# 4. for the amount of rolls the user input
#    A. roll 2 six faced dies
#    B. add the 2 numbers of the dies together and store the sum
#    C. based on the sum add one to the total of the index in the list where the sum is located
# 5. Output numbers rolled seperated by line and print a * per every times rolled for that sum
