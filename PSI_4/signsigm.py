import numpy as np

class SignSigm:
    def __call__(self,alfa):
        def signSigm(x):
            return (2.0/(1.0+np.exp(-alfa*x)))-1.0
        signSigm.__name__+='({0:.3f})'.format(alfa)
        return signSigm
    def derivative(self,alfa):
        def signSigmDeriv(x):
            return 2.0*alfa*np.exp(-alfa*x)/((1.0+np.exp(-alfa*x))**2)
        signSigmDeriv.__name__+='({0:.3f})'.format(alfa)
        return signSigmDeriv

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
    
class Linear:
    def __call__(self):
        def linear(x):
            return x
        return linear
    def derivative(self):
        def linearDeriv(x):
            return 1
        return linearDeriv