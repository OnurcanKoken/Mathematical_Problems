def isIn(char, aStr):
    
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    x = len(aStr)
    x = x//2

    if char == aStr[int(x)]:
        return True
    elif char < aStr[int(x)]:
        return isIn(char, aStr[:x])
    else:
        return isIn(char, aStr[x+1:])

#lets try to find a char in a str
print(isIn("a","qweqweqwe"))