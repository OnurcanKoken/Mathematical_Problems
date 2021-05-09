# köken
# date: 23.04.2021 (dd/mm/yyyy)

class Calculator:
    def power(self, n, p):
        try:
            if (n>=0) and (p>=0):
                return pow(n,p)
            else:
                return "n and p should be non-negative"
        except:
            return "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)