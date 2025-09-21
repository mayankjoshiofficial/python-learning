# Program 01: Reverse of a Number
# Author: Mayank Joshi
# Date: 21-09-2025
# Description: Program to find reverse of a given number.

#UserInput
num = int(input("Enter a number: "))

# validation : number greater than ZERO
while num <= 0:
    num = int(input("Enter a number greater than 0: "))

original_num = num
reverse = 0

while num > 0:                                  
    lastdigit = num % 10                        
    reverse = reverse * 10 + lastdigit         
    num //= 10                                   

print(f"Reverse of {original_num} is: {reverse}")
