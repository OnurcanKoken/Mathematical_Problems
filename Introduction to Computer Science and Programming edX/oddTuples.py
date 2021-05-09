"""
19.04.09
onurcan koken
"""
def oddTuples(aTup):
    newTuple = ()
    i = 0
    while i < len(aTup):
        if i%2 == 0:
            newTuple += (aTup[i],)
        i += 1
    return newTuple

t1 = ('I', 'am', 'a', 'test', 'tuple',2,3)
print(oddTuples(t1))