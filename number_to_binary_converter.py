# convert number to binary
"""
Created on Sat Oct 27 09:09:43 2018

@author: onurcan_koken
"""
x = int(input("enter an int number: "))

while True:
    
    if x < 0:
        neg = True
        x = abs(x)
    else:
        neg = False
    result = ""
    
    if x == 0:
        result = "0"
    while x > 0:
        result = str(x%2) + result
        x = x//2
    if neg:
        result = "-" + result
    print("Here is your result:", result)
    print("If you want to exit enter 'a' ")
    x = input("enter an int number: ")
    if x == 'a':
        break
    else:
        x = int(x)