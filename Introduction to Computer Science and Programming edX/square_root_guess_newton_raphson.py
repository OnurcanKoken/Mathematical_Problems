# newton_raphson_guess
"""
Created on Sun Oct 28 08:02:43 2018

@author: koken
"""
epsilon = 0.01
y = 17.0 #the number that is given
guess = y/2.0 #like bisection search
numGuesses = 0
# if polinomial is x^2 + k then derivative is 2x
# Newton - Raphson says given g for root, 
# a better guess is guess - (guess^2 - k)/(2*guess)
while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print("number of guesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))