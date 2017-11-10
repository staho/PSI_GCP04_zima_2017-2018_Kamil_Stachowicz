#!/usr/bin/python
import random
from math import exp
from sigm import Sigm
from sign import Sign
import numpy as np

class Perceptron:
    def __init__(self, learning_rate, no_of_inputs, activation_function, activation_function_der):
        self.__dict__['_no_of_inputs'] = no_of_inputs
        self.__dict__['_weights'] = []
        self.__dict__['_inputs'] = []
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_activationFunction'] = activation_function
        self.__dict__['_activationFunctionDer'] = activation_function_der
        self.__dict__['_bias'] = -1 * np.random.ranf()
        self.__dict__['_sum'] = None
        self.__dict__['_error'] = None

        for weight in range(0, self._no_of_inputs):
            self._weights.append(random.uniform(-1,1))


    def guess(self, inputs):
        self._inputs = inputs

        self._sum = np.dot(self._weights, self._inputs) + self._bias

        return self._activationFunction(self._sum)

    def train(self, inputs, desiredOutput):
        output = self.guess(inputs)
        delta = (desiredOutput - output)
        self._error = delta * self._activationFunctionDer(self._sum)

        for i in range(len(self._inputs)):
            self._weights[i] += self._error * self._inputs[i] * self._learningRate

        self._bias = self._learningRate * self._error

        return output
