# Program 03: Sum of Digits
# Author: Mayank Joshi
# Date: 19-09-2025
# Description: Calculate sum of digits of a given number.

#input
num = int(input("Enter a number (2 or more digits): "))

#Validation:
while num < 10:
    num = int(input("Enter a positive number with 2 or more digits: "))

original_number = num
total_sum = 0

while num > 0:
    digit = num % 10           # Get last digit
    total_sum += digit         
    num //= 10                 # remove last digit

print(f"Total sum of digits of {original_number} is: {total_sum}")
