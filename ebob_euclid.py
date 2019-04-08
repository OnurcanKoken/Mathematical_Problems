"""
onurcan koken
18.03.2019
"""

def gcdRecur(a,b):

    minimum = min(a,b)
    maximum = max(a,b)

    if (maximum % minimum == 0):
        return minimum
    else:
        return gcdRecur(minimum, maximum % minimum)

print(gcdRecur(24,9))