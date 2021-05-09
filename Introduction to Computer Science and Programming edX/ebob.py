"""
onurcan koken
18.03.2019
"""

def gcdIter(a,b):
    testValue = min(a,b)

    # Keep looping until testValue divides both a & b
    while a % testValue != 0 or b % testValue !=0:
        testValue -= 1
    
    return testValue

print(gcdIter(240,90))