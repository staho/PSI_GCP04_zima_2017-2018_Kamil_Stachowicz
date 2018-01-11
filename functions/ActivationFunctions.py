import numpy as np
import math

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

"""Funkcja licząca odległość"""
def distanceBetweenVectors(vector1, vector2):
    v1len = len(vector1)
    v2len = len(vector2)

    if v1len == v2v2len:
        distSum = 0
        for i in range(v1len):
            distSum += (vector1[i] - vector2[i])**2
        return math.sqrt(distSum)

def distanceBetweenPoints(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1 - y2)**2)
