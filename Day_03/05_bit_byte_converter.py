# Program 05: Bytes Converter
# Author: Mayank Joshi
# Date: 17-09-2025
# Description: Convert Bytes to Bits, Kilobytes, and Megabytes.

# Take input from user
bytes_value = int(input("Enter the number of bytes: "))

# Validation
while bytes_value < 0:
    bytes_value = int(input("Enter a positive number of bytes: "))

# Calculations
bits = bytes_value * 8
kilobytes = bytes_value / 1024
megabytes = bytes_value / (1024 * 1024)

# Print results
print(f"{bytes_value} Bytes is equal to:")
print(f"{bits} Bits")
print(f"{kilobytes:.2f} Kilobytes")
print(f"{megabytes:.4f} Megabytes")
