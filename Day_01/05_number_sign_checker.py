# Program 5: Number Check + or -
# Author: Mayank Joshi
# Date: 15-09-2025

# step1: Takes input from the user

number=int(input("Enter the number : "))

#step2: Conditional statement and checking the number:

if (number<0):
    print(f"{number} is a Negative number")
elif(number>0):
    print(f"{number} is a Positive number ")
else:
    print(f" {number} : Zero")