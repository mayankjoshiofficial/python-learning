# Program 3: Multiplication Table
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Printing the multiplication table of a given number.

# Step 1: Take input
number = int(input("Enter the number: "))

# Step 2: Validate input
while number <= 0:
    number = int(input("Number must be positive and > 0. Enter again: "))

# Step 3: Print table
print(f"\nMultiplication Table of {number}:")
print("-------------------------")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
