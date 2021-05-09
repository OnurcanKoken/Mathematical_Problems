# köken
# date: 26.04.2021 (dd/mm/yyyy)
# example: n = 25, The divisors of 25 are 1, 5, 25. Their sum is 31
# example: n = 20, The divisors of 20 are 1, 2, 4, 5, 10, 20. Their sum is 42

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.list_num = []
        pass

    def divisorSum(self, n):

        for i in range(1,n+1):

            if (n%i) == 0:
                self.list_num.append(i)

        return sum(self.list_num)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)