# Program 2: Sum of Numbers from 1 to N
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Takes input N, validates, and computes sum of 1+2+...+N.

# Step 1: Take input
numbers = int(input("Enter the range of numbers: "))

# Step 2: Validate
while numbers <= 0:
    numbers = int(input("Number must be positive and > 0, Enter Again: "))

# Step 3: Initialize sum
total_sum = 0

# Step 4: Loop and add numbers
for i in range(1, numbers + 1):
    total_sum += i

# Step 5: Print result
print(f"Total sum from 1 to {numbers}: {total_sum}")
