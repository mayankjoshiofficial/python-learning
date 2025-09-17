# Program 3: Factorial (Multiple Calculations)
# Author: Mayank Joshi
# Date: 17-09-2025
# Description: Keep asking user for numbers and calculate factorial until user enters 0.

while True:
    num=int(input("enter a number to find factorial (0 to stop): "))


    if num == 0:
        print("Exiting Program...Thanks for using.")
        break
    if num<0:
        print("please enter positive number ")
        continue

    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"The factorial of {num} is : {fact}")
    print("-"*30)

