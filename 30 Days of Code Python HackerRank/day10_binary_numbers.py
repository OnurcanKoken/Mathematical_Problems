# köken
# date: 23.02.2021 (dd/mm/yyyy)

# return the maximum number of consecutive 1's of the input number

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
import sys


def binary_conversion(n):
    binary_conversion_of_n = []
    while(n>0):
        remainder = n%2
        print("remainder: ", remainder)
        # 4.9 -> 4, 6.1 -> 6
        n = math.floor(n/2)
        print("n: ", n)
        binary_conversion_of_n.insert(0,remainder)
        print("\n")
    return binary_conversion_of_n

def consecutive_1s(binary_n):
    max_consecutive = [(x[0], len(list(x[1]))) for x in itertools.groupby(binary_n)]
    print("max consecutive", max_consecutive)
    return max(max(max_consecutive, key=lambda x:x[:])[:])

if __name__ == '__main__':
    n = int(input())
    # find the binary conversion of given n
    if n == 0:
        print(0)
        sys.exit()

    binary_n = binary_conversion(n)
    print(binary_n)
    num_max_consecutive_1s = consecutive_1s(binary_n)
    print(num_max_consecutive_1s)
