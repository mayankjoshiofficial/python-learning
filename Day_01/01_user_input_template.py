# Program 1: User Input and replace string Template
# Author : Mayank Joshi
# Date : 13-09-2025
# Description: Takes username , validates length >=3 , and replaces <<USERNAME>>

template= "Hello <<Username>> , How are you?"
name=input("Enter your name: ")

#validates:

while len(name) < 3:
    name=input("Name must have at least 3 characters. ENTER AGAIN : ")

greeting=template.replace("<<Username>>",name)
print(greeting)