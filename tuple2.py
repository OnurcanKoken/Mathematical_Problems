x = (1, 2, (3, 'John', 4), 'Hi')
print(x[0])
print(x[2])
print(x[-1])
print(x[2][2])
print(x[-1][-1])
# print(x[-1][2]) error
print(x[0:1])
print(x[0:-1])
print(2 in x) # true
print(3 in x) # false
# print x[0] = 8 error