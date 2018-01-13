from NeuronKohonen import *
import sys
import math

sys.path.append('../functions')
from ActivationFunctions import *


"""Klasa sieci Kohonena"""
class Grid:
    """Klasa tworząca neurony i ustawiająca parametry sieci"""
    def __init__(self, noOfInputs, learningRate, height, width, nbRay):
        self.__dict__['_noOfInputs'] = noOfInputs
        self.__dict__['_learningRate'] = learningRate
        self.__dict__['_height'] = height
        self.__dict__['_width'] = width
        self.__dict__['_neurons'] = [[NeuronKohonen(self._learningRate, self._noOfInputs, x, y) for x in range(self._width)] for y in range(self._height) ]
        self.__dict__['_neighbourhoodRay'] = nbRay
        self.__dict__['_gaussDivisor'] = 2 * nbRay**2

    """Funkcja trenowania sieci"""
    def train(self, inputs):
        winner = self.guess(inputs)

        for i in range(self._height):
            for j in range(self._width):
                tempNeuron = self._neurons[i][j]
                g = self.gaussNeighbourhood(winner=winner, neighbour=tempNeuron)
                tempNeuron.trainGauss(g)

        return winner

    """Funkcja wyłaniająca najsilniejszy neuron"""
    def guess(self, inputs):
        lowestOutput = 10
        winnerCoords = (0,0)
        for i in range(self._height):       #wybierany zostaje neuron o najmniejszej odleglosci wektorow: wejscia od wag
            for j in range(self._width):
                tmp = self._neurons[i][j].guess(inputs)
                if tmp < lowestOutput:
                    lowestOutput = tmp
                    winnerCoords = (i, j)

        return self._neurons[winnerCoords[0]][winnerCoords[1]]

    """Funkcja przywracająca początkowe wagi neuronów"""
    def resetNeurons(self):
        for i in range(self._height):
            for j in range(self._width):
                self._neurons[i][j].resetNeuron()

    """Funkcja sąsiedztwa Gaussowskiego"""
    def gaussNeighbourhood(self, winner, neighbour):
        dx = winner.getX() - neighbour.getX()
        dy = winner.getY() - neighbour.getY()

        return math.exp(-(dx**2 + dy**2)/self._gaussDivisor)
