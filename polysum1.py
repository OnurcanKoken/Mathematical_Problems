import math
from polysum import *

n = int(input('Give an n: '))
s = int(input('Give an s: '))

#area = (0.25 * n * s**2)/(math.tan(math.pi/n))
#perimeter = n*s
#print(round(area + perimeter**2, 4))

print(polysum(n,s))