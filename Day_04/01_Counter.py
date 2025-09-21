# Program 01: Count Digits in a Number
# Author: Mayank Joshi
# Date: 21-09-2025
# Description: Count how many digits are in the given number.

num = int(input("Enter a number: "))

# Validation
while num <= 0:
    num = int(input("Enter a positive number greater than 0: "))

count = 0

while num > 0:
    num //= 10   # removes last digit each time
    count += 1   # count increases by 1

print(f"Number of digits: {count}")
