# Program 4: Sum of Even Numbers
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Calculate the sum of all even numbers between a given range.

# Step 1: Take input
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Step 2: Validation
while end <= start:
    print(" Ending range must be greater than starting range.")
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))

# Step 3: Calculate sum
total_sum = 0
for i in range(start, end + 1):  # include the end value
    if i % 2 == 0:
        print(i)
        total_sum += i  # shorthand for total_sum = total_sum + i

# Step 4: Print result
print("-----------------")
print(f"Sum of even numbers from {start} to {end} is: {total_sum}")
