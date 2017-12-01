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