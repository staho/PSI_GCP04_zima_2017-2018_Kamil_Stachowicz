import random

class TestPoint:

    def __init__(self):
        self.x = self.sign(random.uniform(-1,1))
        self.y = self.sign(random.uniform(-1,1))

        if self.x == 1 and self.y == 1:
            self.match = 1
        else:
            self.match = -1

    def sign(self, x):
        if x >= 0:
            return 1
        else:
            return -1
