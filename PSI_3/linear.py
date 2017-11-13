import numpy as np
class Linear:
    def __call__(self, a):
        def linear(x):
            return x
        linear.__name__ += '({0:.3f})'.format(a)
        return linear
    def derivative(self, a):
        def linearDer(x):
            return 1
        linearDer.__name__ += '({0:.3f})'.format(a)
        return linearDer
