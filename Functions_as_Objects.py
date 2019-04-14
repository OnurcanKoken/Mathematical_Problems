"""
19.04.14
onurcan koken
Functions as Objects
"""
from factorial import *
from fibonacci_rabbit import *

def applyToEach(L,f):
    """
    assumes L is a list, f is a function
    mutates L by replacing each element,
    e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.4, 3.5]

applyToEach(L, abs)
print(L)
applyToEach(L, int)
print(L)
applyToEach(L, fact)
print(L)
applyToEach(L, fib)
print(L)

# using funtions in a list
def applyFuns(L,x):
    for f in L:
        print(f(x))

applyFuns([abs, int, fact, fib], 4)

# generalization of hops
# produces an iterable
for elt in map(abs, [1, -2, 3, -4]):
    print(elt)
a = map(abs, [1, -2, 3, -4])
print(a) # there is no return!

# here is a better way to use for an n-ary function
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, L1, L2):
    print(elt)

testList = [1, -4, 8, -9]

def timesFive(n):
    return n*5
applyToEach(testList, timesFive)

testList = [1, -4, 8, -9]

def sortedAbsList(n):
    testList_copy = testList[:]
    i = 0
    for elt in map(abs, testList_copy):
        testList[i] = elt
        i += 1
    testList.sort()
sortedAbsList(testList)
print(testList)

testList = [1, -4, 8, -9]

def increaseList(n):
    testList_copy = testList[:]
    i = 0
    for elt in testList_copy:
        testList[i] = elt + 1
        i += 1
increaseList(testList)
print(testList)

testList = [1, -4, 8, -9]

def squareList(n):
    testList_copy = testList[:]
    i = 0
    for elt in testList_copy:
        testList[i] = elt*elt
        i += 1
squareList(testList)
print(testList)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))