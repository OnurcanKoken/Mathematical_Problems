# 13th of May, 2021
# Onurcan Köken

state = "not bad"

def myfeel_1():
    print("Currently " + state)

def myfeel_2():
    # this gives an error since there is a local variable in this function
    # print("Currently " + state)
    # local variable
    state = "getting better"
    print("Currently " + state)

def my_feel_3():
    # create global variable inside of a function
    global state
    state = "much better"

myfeel_1()
myfeel_2()
# still global version is on
print("Currently " + state)

# global variable inside a function
my_feel_3()
print("Currently " + state)

# reference: https://www.w3schools.com/python/python_variables_global.asp