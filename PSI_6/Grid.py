from NeuronKohonen import *
import sys
import math

sys.path.append('../functions')
from ActivationFunctions import *


"""Klasa sieci Kohonena"""
class Grid:
    """Klasa tworząca neurony i ustawiająca parametry sieci"""
    def __init__(self, noOfInputs, learningRate, height, width, nbMaxRay, nbMinRay, epochs):
        self.__dict__['_noOfInputs'] = noOfInputs
        self.__dict__['_learningRate'] = learningRate
        self.__dict__['_height'] = height
        self.__dict__['_width'] = width
        self.__dict__['_neurons'] = [[NeuronKohonen(self._learningRate, self._noOfInputs, x, y) for x in range(self._width)] for y in range(self._height) ]
        self.__dict__['_neighbourhoodMaxRay'] = nbMaxRay
        self.__dict__['_neighbourhoodMinRay'] = nbMinRay
        self.__dict__['_epochs'] = epochs
        self.__dict__['_gaussDivisor'] = 2 * nbMaxRay**2
        self.__dict__['_currentRay'] = nbMaxRay

    """Funkcja trenowania sieci"""
    def train(self, inputs, currEpoch):
        winner = self.guess(inputs)

        for i in range(self._height):
            for j in range(self._width):
                tempNeuron = self._neurons[i][j]
                g = self.gaussNeighbourhood(winner=winner, neighbour=tempNeuron)
                tempNeuron.trainGauss(g)    #za każdym razem uczone są wszystkie neurony
                                            #uwzględniając odpowiedni współczynnik G

        self.calculateRay(currEpoch)
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

    """Funkcja zmnieniająca promień sąsiedztwa"""
    def calculateRay(self, epoch):
        self._currentRay = self._neighbourhoodMaxRay * (self._neighbourhoodMinRay/self._neighbourhoodMaxRay)**(epoch/self._epochs)
        self._gaussDivisor = 2 * self._currentRay ** 2
