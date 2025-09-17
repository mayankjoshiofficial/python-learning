# Program 2: Product of Numbers
# Author: Mayank Joshi
# Date: 17-09-2025
# Description: Calculate the product of numbers in a given range.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

product = 1

for i in range(start, end + 1):
    product *= i

print(f"Product of numbers from {start} to {end} is: {product}")
