# Program 01: 
# Author: Mayank Joshi
# Date: 30-09-2025
# Description: Searching number in an Array Function.


# Function :
def searchArr(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[1,4,1,3,5,6,7,8,3,9,2,8]
x=5
s=searchArr(arr,x)
print(f"Index poistion of number into an Arr is: {s}")
