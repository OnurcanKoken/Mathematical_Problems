def mult(a,b):
    if b==1:
        return a
    else:
        return a + mult(a,b-1)

a = 5
b = 4

print(mult(a,b))
