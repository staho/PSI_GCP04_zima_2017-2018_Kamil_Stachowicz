import random
from math import exp
from signsigm import *
import numpy as np

class Neuron:
    def __init__(self, iid, learning_rate, no_of_inputs, activation_function, forgetRate):
        self.__dict__['_no_of_inputs'] = no_of_inputs
        self.__dict__['_weights'] = []
        self.__dict__['_inputs'] = []
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_activationFunction'] = activation_function
        self.__dict__['_bias'] = -0.5
        self.__dict__['_forgetRate'] = forgetRate
        self.__dict__['_sum'] = None
        self.__dict__['_error'] = None
        self.__dict__['_startingWeights'] = []
        self.__dict__['_val'] = 0
        self.__dict__['_iid'] = iid

        for weight in range(0, self._no_of_inputs):
            self._weights.append(np.random.uniform(-1, 1))
        if self._forgetRate == None:
            self._forgetRate = 0

        for weight in self._weights:
            self._startingWeights.append(weight)

    def guess(self, inputs):
        self._inputs = inputs

        self._sum = np.dot(self._weights, self._inputs) + self._bias
        self._val = self._activationFunction(self._sum)
        return self._val

    def trainWithSupervisor(self, inputs, desiredOutput):  #∂wij(k+1) = (1-fr)*∂wij(k) + lr*yj*yi (yj to wejście nr j) yi to oczekiwane wyjscie
        output = self.guess(inputs)

        for i in range(len(self._inputs)):           
            self._weights[i] = (1-self._forgetRate) * self._weights[i] + self._learningRate * self._inputs[i] * desiredOutput

    def trainWithoutSupervisor(self, inputs): #∂wij(k+1) = (1-fr)*∂wij(k) + lr*yj*yi (yj to wejście nr j) yi to wyjście neuronu
        output = self.guess(inputs)

        constant = self._learningRate * output
        forget = (1-self._forgetRate)
        for i in range(len(self._inputs)):           
            self._weights[i] *= forget
            self._weights[i] += constant * self._inputs[i]
        
        return output

    def resetWeights(self):
        self._weights = []
        for weight in self._startingWeights:
            self._weights.append(weight)