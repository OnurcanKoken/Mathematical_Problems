# köken
# date: 24.02.2021 (dd/mm/yyyy)

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

if __name__ == '__main__':
    # use the following to input 6x6 arr array
    #arr = []
    #for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))

    # let us try this one
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    # or this one, as you wish
    #arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]
    # hourglass key
    key = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    # hourglass sum variables
    # these are the min. limits for this case
    hourglass_sum = -99999
    hourglass_sum_max = -99999
    # find max hourglass sum
    for i in range(0,4):
        for j in range(0,4):
            hourglass_sum_1 = arr[i][j]*key[0][0] + arr[i][j+1]*key[0][1] + arr[i][j+2]*key[0][2]
            hourglass_sum_2 = arr[i+1][j]*key[1][0] + arr[i+1][j+1]*key[1][1] + arr[i+1][j+2]*key[1][2]
            hourglass_sum_3 = arr[i+2][j]*key[2][0] + arr[i+2][j+1]*key[2][1] + arr[i+2][j+2]*key[2][2]
            hourglass_sum = hourglass_sum_1 + hourglass_sum_2 + hourglass_sum_3
            if hourglass_sum > hourglass_sum_max:
                hourglass_sum_max = hourglass_sum
                print("hourglasses for each max", hourglass_sum_1, hourglass_sum_2, hourglass_sum_3)
    print(hourglass_sum_max)