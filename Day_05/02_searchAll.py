# Program 02:
# Author: Mayank Joshi
# Date: 01-10-2025
# Description: Find all index positions of a number in an Array.

def searchAll(arr, x):
    indices = []
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
    return indices

arr = [1, 4, 1, 3, 5, 6, 7, 8, 3, 9, 2, 8]
x = 8
result = searchAll(arr, x)

if result:
    print(f"{x} found at positions: {result} ")
else:
    print(f"{x} not found in array.")
