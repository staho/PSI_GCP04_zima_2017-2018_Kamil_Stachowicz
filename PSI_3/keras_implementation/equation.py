import math


class Equation:
    def getValue(x, y):
        return 20 + x**2 + y**2 - 10 * (math.cos(math.pi*2*x) + math.cos(math.pi*2*y))
