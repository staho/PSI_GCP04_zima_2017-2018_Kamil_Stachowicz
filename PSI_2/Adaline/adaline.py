#!/usr/bin/python
import random
import numpy as np
from enum import Enum

class Adaline:
    class AdalineType(Enum):
        MAJORITY = 0
        AND = 1
        OR = 2

    def __init__(self, learning_rate, no_of_inputs, typeOfAdaline):
        self.__dict__['_no_of_inputs'] = no_of_inputs
        self.__dict__['_typeOfAdaline'] = typeOfAdaline
        self.__dict__['_weights'] = []
        self.__dict__['_inputs'] = []
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_bias'] = 1
        self.__dict__['_sum'] = None
        self.__dict__['_error'] = None

        for weight in range(0, self._no_of_inputs):
            self._weights.append(random.uniform(-1,1))

        print("Learning rate = ", self._learningRate, "num of inputs: ", self._no_of_inputs)


    def guess(self, inputs):
        self._inputs = inputs

        self._sum = np.dot(self._weights, self._inputs) + self._bias

        return self.sign(self._sum)

    def train(self, inputs, desiredOutput):
        output = self.guess(inputs)

        print("Train info: output: ",output,", desired: ",desiredOutput)

        self._error = desiredOutput - self._sum


        for i in range(len(self._inputs)):
            self._weights[i] += self._error * self._inputs[i] * self._learningRate

        self._bias = self._learningRate * self._error

    def sign(self, x):
        if self._typeOfAdaline == Adaline.AdalineType.OR:
            if x >= (self._noOfInputs - 1) :
                return 1
            else:
                return -1
        elif self._typeOfAdaline == Adaline.AdalineType.OR:
            if x >= (1 - self._noOfInputs) :
                return 1
            else:
                return -1
        elif self._typeOfAdaline == Adaline.AdalineType.MAJORITY:
            if x > 0:
                return 1
            else:
                return -1
