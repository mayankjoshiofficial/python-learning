#Program 2: Flip coin and Print percentage of Heads and Tails
#Author : Mayank Joshi
#Date: 15-09-2025
#Description : Takes number of Flips, simulates coin flip , prints percentage of Heads/Tails.


import random 

#Step 1: Take input

flips=int(input("Enter number of times to flip the coin: "))


#Validate input
while(flips <=0):
    flips = int(input("Enter a positive number: "))

#step 2: Initialize counters
heads = 0
tails =0

#step 3: Loop and flip

for i in range(flips):
    if random.randint(0,1) == 1:
        heads+=1
    else :
        tails+=1

# step 4: Calculate percentages
heads_percent =(heads/flips)*100
tails_percent =(tails/flips)*100


# step 5: Printing results 
print("=============================")
print()
print(f"total heads: {heads}")
print(f"total  tails: {tails}")
print("------------------------------")
print("TOTAL PERCENTAGE ")
print(f"Heads : {heads_percent: .2f}%")
print(f"Tails:{tails_percent: .2f}%")


