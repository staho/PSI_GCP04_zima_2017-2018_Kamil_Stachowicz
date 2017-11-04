#!/usr/bin/python

from perceptron import Perceptron

class SingleLayer:

    availableLetters = ['a', 'b', 'o', 'A', 'B', 'C', 'D']

    def __init__(self, no_of_perceptrons, no_of_inputs, learning_rate, activation_function, activation_function_der):
        self.__dict__['_perceptrons'] = []
        self.__dict__['_testInputs'] = []
        self.__dict__['_activationFunction'] = activation_function
        self.__dict__['_activationFunctionDer'] = activation_function_der
        self.__dict__['_noOfInputs'] = no_of_inputs
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_noOfPerceptrons'] = no_of_perceptrons

        for i in range(self._noOfPerceptrons):
            self._perceptrons.append(self._learningRate, self._noOfInputs, self._activationFunction, self._activationFunctionDer)

    def getPerceptron(self, index_of_perceptron):
        if(index_of_perceptron < 0 or index_of_perceptron >= len(self._perceptrons)):
            return None
        else:
            return self._perceptrons[index_of_perceptron]
    def trainPercpeptrons(self):
        i = 0
        perceptron_counter = 0

        for perc in self._perceptrons:
            perc.train(
                self._testInputs[i]._testArguments,
                self._testInputs[i]._desiredOutputs[perceptron_counter]
            )
            perceptron_counter += 1
            if perceptron_counter == len(self._perceptrons)
            i += 1
            if i == len(self._testInputs):
                i = 0

    def makeTestInputs(self, no_of_tests):
        x = 0
        for i in range(0, no_of_tests):
            self._testInputs.append(TestInput(availableLetters[x]))
            x += 1
            if x == len(availableLetters):
                x = 0
