# köken
# date: 20.02.2021 (dd/mm/yyyy)

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    """
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    """
    n = 4
    arr = [1, 4, 3, 2]
    print(arr)
    reversed_arr = ""
    while(n!=0):
        n -= 1
        reversed_arr = reversed_arr + str(arr[n]) + " "
    print(reversed_arr)

    """ # to reverse a number in an array
    arr = int(arr[0])

    reversed = 0
    while (arr != 0):
        temp = int(arr % 10)
        reversed = reversed * 10 + temp
        arr = int(arr / 10)

    print(reversed)
    """