# Program 05: Factorial of a Number
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Calculates the factorial of a given positive number.

# Take user input
num = int(input("Enter a number: "))

# Validation
while num <= 0:
    num = int(input("Please enter a positive number greater than 0: "))

# Calculate factorial
fact = 1
for i in range(1, num + 1):
    fact *= i

# Display result
print(f"The factorial of {num} is {fact}")
