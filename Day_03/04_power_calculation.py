# Program 4: Manual Power Calculation
# Author: Mayank Joshi
# Date: 17-09-2025
# Description: Calculate x^y (x raised to the power y) without using ** operator.
#In mathematical terms : Exponential of a number
print("x^y y is the power/ exponent")
print("-"*30)
x = int(input("Enter base number (x): "))
y = int(input("Enter exponent (y): "))

result = 1

for i in range(y):
    result *= x

print(f"{x}^{y} = {result}")
print("-"*30)
