import random
import numpy as np
import math
"""Klasa neuronu według Kohonena"""
class NeuronKohonen:
    """Funkcja inicjalizująca - ustawianie parametrów neuronu"""
    def __init__(self, learning_rate, no_of_inputs, x, y):
        self.__dict__['_no_of_inputs'] = no_of_inputs
        self.__dict__['_weights'] = []
        self.__dict__['_inputs'] = []
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_sum'] = None
        self.__dict__['_weightsStart'] = []
        self.__dict__['err'] = None
        self.__dict__['_x'] = x
        self.__dict__['_y'] = y


        for i in range(self._no_of_inputs):     #losowanie wag i zapisanie ich kopii
            weight = random.uniform(0,1)
            self._weights.append(weight)
            self._weightsStart.append(weight)

    """Funkcja procesująca"""
    def guess(self, inputs):
        self._inputs = inputs
        self._sum = 0

        for i in range(len(self._weights)):     #wyjsciem neuronu jest odległość między wagami a danymi wejściowymi
            self._sum += (self._inputs[i] - self._weights[i])**2
        self._sum = math.sqrt(self._sum)

        return self._sum
    """Funkcja trenująca - uaktualniająca wagi"""
    def train(self):
        errTemp = 0
        for i in range(len(self._inputs)):  #aktualizacja wag polega na przyblianiu ich do wektora wejściowego
            self._weights[i] += self._learningRate * (self._inputs[i] - self._weights[i])

    def trainGauss(self, error):
        tmp = error * self._learningRate
        for i in range(len(self._inputs)):  #aktualizacja wag polega na przyblianiu ich do wektora wejściowego
            self._weights[i] += tmp * (self._inputs[i] - self._weights[i])

    """Funkcja zwracająca wagi jako string"""
    def getWeightsAsString(self):
        return str(self._weights)

    """Funkcja resetująca wagi neuronów do początkowych"""
    def resetNeuron(self):
        self._weights = []
        for weight in self._weightsStart:
            self._weights.append(weight)

    """Funkcja odleglosci pomiedzy neuronami"""
    def getDistanceToOther(self, other):
        return math.sqrt((self._x-other.getX())**2 + (self._y - other.getY())**2)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getNeuronString(self):
        return "x: " + str(self._x) + " y: " + str(self._y)
