"""
onurcan koken
18.03.2019
"""

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
            print(ans)
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))

print("Is eve a palidrome?")
print(isPalindrome("eve"))

print("")
print("Is able was I ere I saw Elba a palidrome?")
print(isPalindrome("Able was I, ere I saw Elba"))