# guess_secret_number
"""
Created on Wed Oct 24 11:33:39 2018

@author: onurcan_koken
"""

x=int(input('Please think of a number between 0 and 100!'))
low=0
high=100
ans=(high + low)//2
epsilon=1.0

while True:
    print("Is your secret number",ans,"?")
    y=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if y == 'c':
        break
    elif y == 'h':
        high = ans
    elif y == 'l':
        low = ans
    else:
        print("there is a problem")
    ans = (high + low)//2
print("Game over. Your secret number was:",ans)