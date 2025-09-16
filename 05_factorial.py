# Program 5: Factorial Calculator
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Calculate factorial of a given number using a for loop.

print("Factorial Program")
num = int(input("Enter the number: "))

# Validation
while num < 0:
    num = int(input("Factorial is not defined for negative numbers. Enter again: "))

fact = 1
for i in range(1, num + 1):
    fact = fact * i

print(f"Factorial of {num} is: {fact}")
