# Program 3: Voting Eligibility Checker
# Author: Mayank Joshi
# Date: 15-09-2025
# Description: Takes age as input, validates it, checks if user is eligible to vote.

# Step 1: Input
age = int(input("Enter your age: "))

# Step 2: Validate (must be positive number)
while age <= 0:
    age = int(input("MUST BE A POSITIVE INTEGER, Try Again: "))

# Step 3: Check voting eligibility
if age >= 18:
    print("🎉 Congratulations! You are eligible to vote.")
else:
    print("⚠ You are under 18, NOT eligible to vote.")
