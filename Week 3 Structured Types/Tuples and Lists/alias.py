"""
19.04.11
onurcan koken
alias clone mutation
"""

warm = ['red', 'yellow', 'orange']
hot = warm # aliasing
"""
here hot is an alias for warm - changing one changes the other!!!
they are pointing the same object, list
"""
print(warm)
print(hot)

hot.append('pink')
print(warm)

# these two lists print out the same thing but these are not pointing the same object
cool = ['black', 'pink']
chill = ['black', 'pink'] 
# they are not the same

"""
clonning a list
"""
cool = ['blue', 'green', 'black']
chill = cool[:] # clonning, they are not pointing the same object
print(chill)

nlist = [cool] # nested list
print(nlist)
nlist.append(warm)
print(nlist)
warm.append('blue')
print(nlist)
print(nlist+cool+warm)

L1 = [1,2,3,4]
L2 = [1,2,5,6]


def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
remove_dups(L1,L2)
print(L1)
"""
now, after removing '1'
we couldnt removed '2'
since we mutated the list, the size is changed
after '1' we checked '3'
and we missed '2'
so to avoid this, we will make a copy
"""

L1.insert(0,1) # insert an element to list by index add '1' as '0'th element
print(L1)
def remove_dups(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
remove_dups(L1,L2)
print(L1)
print(L1 is L2) # false

clist = [1,2,3,4,5,6]
dlist = []
for num in clist:
    dlist.append(num)
print(clist == dlist) # true
print(clist is dlist) # false
print(dlist)

dlist = clist # aliasing
print(clist is dlist) # true
print(dlist)