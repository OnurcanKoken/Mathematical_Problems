# onurcan köken
# date: 15.02.2021 (dd/mm/yyyy)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_cost = round(meal_cost + meal_cost*tip_percent/100 + meal_cost*tax_percent/100)
    print(total_cost)
    return total_cost

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
