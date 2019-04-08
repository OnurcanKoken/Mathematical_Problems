import math
# to be able to use tan() and pi

def polysum(n,s):

    # n indicates number of sides
    # s indicates lenght of each side
    area = ((0.25 * n * s**2)/math.tan(math.pi/n)) # area of the polygon
    perimeter = n*s # perimeter of the polygon
    return round(area + perimeter**2, 4)