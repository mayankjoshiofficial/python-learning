# Program 3: Age Checker
# Author: Mayank Joshi
# Date: 15-09-2025
# Description: Takes user age, checks if adult, teenager, or child

# Step 1: Take input
age = int(input("Enter your age: "))

# Step 2: Validate input
while age <= 0:
    age = int(input("Age must be positive. Enter again: "))

# Step 3: Decision making
if age >= 18:
    print("You are an Adult ")
elif age >= 13:
    print("You are a Teenager ")
else:
    print("You are a Child ")
