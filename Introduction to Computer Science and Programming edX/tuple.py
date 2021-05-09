"""
19.04.08
onurcan koken
tuples
"""

te = ()
t2 = (2,"one",3)
print(t2[0]) # display 2
# remember that you can not modify t2[1] = 4 gives an error
t2 += (5,6)
print(t2)
print(t2[1:2])
# ('one') gives you only string but ('one',) is a tuple
# extra comma means this is a tuple
# conveniently used to swap variable values
x = 5
y = 8
(x, y) = (y, x)
t1 = (x, y)
print(t1)
# used to return more than one value from a function
def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q, r)
(quot, rem) = quotient_and_remainder(4, 5)
# can iterate over tuples
def get_data(aTuple): # we will seperate ints and strings
    nums = () # new empty tuple
    words = ()
    for t in aTuple: 
        nums = nums + (t[0],) # first element, integer goes to nums tuple
        if t[1] not in words: # otherwise
            words = words + (t[1],1)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
(small, large, words) = get_data(((1,'mine'),(3,'yours'),(5,'ours'),(7,'mine')))
print(small, large, words)