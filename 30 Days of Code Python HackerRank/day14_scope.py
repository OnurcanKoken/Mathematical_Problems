# köken
# date: 27.02.2021 (dd/mm/yyyy)
import sys

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -sys.maxsize

    # Add your code here
    def computeDifference(self):

        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                self.maximumDifference = max(self.maximumDifference, abs(a[j] - a[i]))


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
