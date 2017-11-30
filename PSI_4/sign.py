class Sign:
    def __call__(self):
        def sign(x):
            if x >= 0:
                return 1
            else:
                return -1
        sign.__name__ += '({0:.3f})'
        return sign
    def derivative(self):
        def signDer(x):
            return 1
        signDer.__name__ += '({0:.3f})'
        return signDer
