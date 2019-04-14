"""
19.04.11
onurcan koken
lists
"""

x = [1, 2, [3, 'John', 4], 'Hi'] 
print(x[2])
print(x[-2])
print(x[2][2]) # be careful
print(2 in x)
print(3 in x)
print(x[0:1]) # be careful
x[0] = 8 # be careful
print(x) 
L = [1,2,3]
L.append('Hi') # object_name.do_smt()
print(L)
print(x+L)
L.extend([0, 6]) # take a list and add it to the end of L
print(L) # mutated 
L.pop() # remove element at end of list
print(L)
L.remove(2) # remove a specific element
i = 2
del(L[i]) # remove a specific element by index
print(L)
s = 'abc'
print(list(s))
s1 = 'I <3 cs'
print(s1.split('<'))
print(s1)
L1 = ['a','b','c']
print(''.join(L1)) # join them together
'_'.join(L1)
print(L1)
print('_'.join(L1))
L1.pop()
print(L1)
L2 = [6, 9, 0, 3]
print(sorted(L2)) # does not mutate L
L2.sort() # mutates L but does not return, return None
print(L2) 
L2.reverse() # mutates L but does not return, return None
print(L2)

#range returns smt that behaves like a tuple
print(range(5))
a = range(3,7,2) # 3 and 5 only
print(a)
for var in a:
    print('o')