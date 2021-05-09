# onurcan köken
# date: 16.02.2021 (dd/mm/yyyy)

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

if N % 2 == 1 or (N > 5 and N < 21):
    print("Weird")
elif (N % 2 == 0)  or (N > 1 and N < 6) or (N > 20):
    print("Not Weird")