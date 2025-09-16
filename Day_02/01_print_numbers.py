# Program 1: Print the numbers
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Printing the numbers using for loop, user input, and validation.

# Takes User Input:
numbers = int(input("Enter the number: "))

# Validation:
while numbers <= 0:
    numbers = int(input("Enter positive number and greater than 0, Enter Again: "))

# Loop from 1 to numbers
for i in range(1, numbers + 1):
    print(i)
