def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    x = x*x*x*x
    # if defined use x= square(x) twice
    return x
x = int(input("give me an x: "))
print("here is your fourthpower of x ", fourthPower(x))