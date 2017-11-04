class Sigm:
    def __call__(self, beta):
        def sigm(x):
            return 1.0/(1.0+np.exp(-beta*x))
        sigm.__name__ += '({0:.3f})'.format(beta)
        return sigm
    def derivative(self, beta):
        def sigmDeriv(x):
            return beta*np.exp(-beta*x)/((1.0+np.exp(-beta*x))**2)
        sigmDeriv.__name__ += '({0:.3f})'.format(beta)
        return sigmDeriv
