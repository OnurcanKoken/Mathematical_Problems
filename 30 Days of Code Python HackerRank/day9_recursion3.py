# köken
# date: 22.02.2021 (dd/mm/yyyy)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
# recursive function
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

