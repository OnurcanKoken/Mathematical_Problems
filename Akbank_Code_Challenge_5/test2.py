#!/bin/python3
# Infinite String 2
# 28.09.2021
# Onurcan Köken

import math
import os
import random
import re
import sys

#
# Complete the 'infiniteString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def infiniteString(s, n):
    # Write your code here
    k_num = 0 # initialize count of k
    s_num = 0 # index for s
    if s == "" or n == 0:
        return 0
    for i in range(n):
        if s[s_num] == "k":
            k_num = k_num + 1
        s_num = s_num + 1
        if s_num == 3:
            s_num = 0
    return k_num # count of k in the substring

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = infiniteString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()