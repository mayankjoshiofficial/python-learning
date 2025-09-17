# Program 4: Sum of Even Numbers
# Author : Mayank Joshi
# Date : 16-09-2025
# Description: Calculate the sum of all even numbers in a given range.

# Step 1: Take user input
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Step 2: Validate input
while start > end:
    print("Starting number must be less than or equal to ending number.")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

# Step 3: Calculate sum of even numbers
total_sum = 0
for i in range(start, end + 1):  # include end number
    if i % 2 == 0:
        print(i, end=" ")
        total_sum += i

# Step 4: Display result
print("\n-----------------")
print(f"Sum of all even numbers from {start} to {end} = {total_sum}")
