# Program 1: Sum of Odd Numbers
# Author: Mayank Joshi
# Date: 17-09-2025
# Description: Calculate the sum of all odd numbers in a given range.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

total_sum = 0

for i in range(start, end + 1):  # include end
    if i % 2 != 0:
        total_sum += i

print(f"Sum of all odd numbers from {start} to {end} is: {total_sum}")
