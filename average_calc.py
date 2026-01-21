#!/usr/bin/env python3
# Created by: Angelo Garcia
# Date Created: January 21, 2026
# This program generates 10 random numbers between 1 and 100.
# It stores the numbers in a list, prints them, and calculates the average.
# The average is computed manually using a loop (no built-in functions).

import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 1
MAX_NUM = 100

# Main program
list_of_int = []

# Generate 10 random numbers and add to the list
for i in range(MAX_ARRAY_SIZE):
    num = random.randint(MIN_NUM, MAX_NUM)
    list_of_int.append(num)

# Display the numbers
print("Numbers:", list_of_int)

# Calculate the average using a loop
total = 0
for num in list_of_int:
    total += num

average = total / MAX_ARRAY_SIZE

# Display the average
print("Average:", average)
