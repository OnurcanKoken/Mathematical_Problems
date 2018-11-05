# square root guess of a random variable
"""
Created on Tue Oct 23 20:15:43 2018

@author: onurcan_koken
"""
while True:
    x = int(input("exit: 0 / enter a random int number: "))
    if x == 0:
        break
    epsilon = 0.01
    num_guess = 0
    low = 1.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
        num_guess += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0    
    print("number of guesses = " + str(num_guess))
    print(str(ans) + " is close to square root of " + str(x))