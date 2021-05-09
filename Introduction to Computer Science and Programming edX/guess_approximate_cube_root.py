# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:31:09 2018

@author: onurcan_koken
"""
while True:
    cube = int(input("Enter a number that will be guessed: "))
    epsilon = 0.01
    guess = 0.0
    increment = 0.0001
    num_guesses = 0
    k = 0
    # just using > can be enough in my opinion
    while abs(guess**3 - cube) >= epsilon:
        guess += increment
        num_guesses += 1
    print("Number of guesses:", num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print("Failed on cube root of", cube)
    else:
        print(guess, "is close to the cube root of", cube)
    k = int(input("Keep going by entering 0: "))
    if k != 0:
        break