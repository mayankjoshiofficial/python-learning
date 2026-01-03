print("******************************************")
print("Question1: Count Occurrences")
arr = [1, 3, 5, 3, 7, 3, 9]
x = 3
# Output: 3 appears 3 times

arr = [1, 3, 5, 3, 7, 3, 9]
x=3
indices=[]
for i in range(len(arr)):
    if arr[i]==x:
        indices.append(i)
print(indices)


print("******************************************")
print("Question2: Find Largest Element (without built-in max())")
# question2: 
arr = [10, 25, 8, 36, 4]
# Output: Largest element = 36

arr = [10, 25, 8, 36, 4,50]
large=0
for i in arr:
    if i>large:
        large=i
print(large)

print("******************************************")
print("Question3:Reverse Array (without [::-1])")

arr = [10, 20, 30, 40]
rev = []

for i in range(len(arr)-1, -1, -1):  # start last → first
    rev.append(arr[i])
print("Original array:",arr)
print("Reversed array:", rev)





print("******************************************")
print("Question4:Reverse Array (without [::-1])")

arr = [8, 6, 2, 5, 4,1]

# Step 1: assume first element is smallest
smallest = arr[0]
index = 0

# Step 2: check each element
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
        index=i

print(f"The smallest number {smallest} is in index {index}")