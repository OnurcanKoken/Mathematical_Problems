"""
19.04.11
onurcan koken
check: https://docs.python.org/2/tutorial/datastructures.html
"""

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print(listA.sort())
print(listA)
print(listA.insert(0, 100))
print(listA)
listA.remove(3)
print(listA)
listA.append(7)
print(listA)
print(listA + listB)
listB.sort()
print(listB)
listB.pop()
print(listB.count('a'))
print(listB)
listA.extend([4, 1, 6, 3, 4])
print(listA)
listA.count(4)
print(listA.index(4))
listA.pop(4)
print(listA)
listA.reverse()
print(listA)