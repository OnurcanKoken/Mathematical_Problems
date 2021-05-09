# köken
# date: 28.04.2021 (dd/mm/yyyy)
# Given an array, a, of size n distinct elements,
# sort the array in ascending order using the Bubble Sort algorithm
# Input: 4 "enter" 4 3 1 2 "enter"
# Output: 1 2 3 4

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def Bubble_Sort(n, a):
    totalNumberOfSwaps = 0
    for i in range(n):
        # Track number of elements swapped during a single array traversal
        numberOfSwaps = 0
        for j in range(n-1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numberOfSwaps += 1
                totalNumberOfSwaps += 1
        # If no elements were swapped during a traversal, array is sorted
        if numberOfSwaps == 0:
            return a, totalNumberOfSwaps
    return a, totalNumberOfSwaps

new_a, swaps = Bubble_Sort(n, a)
print("Array is sorted in", swaps, "swaps.")
print("First Element:", new_a[0], "\nLast Element:", new_a[n-1])
