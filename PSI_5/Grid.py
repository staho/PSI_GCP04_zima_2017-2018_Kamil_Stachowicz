from NeuronKohonen import *

"""Klasa sieci Kohonena"""
class Grid:
    """Klasa tworząca neurony i ustawiająca parametry sieci"""
    def __init__(self, noOfInputs, learningRate, height, width):
        self.__dict__['_noOfInputs'] = noOfInputs
        self.__dict__['_learningRate'] = learningRate
        self.__dict__['_height'] = height
        self.__dict__['_width'] = width
        self.__dict__['_neurons'] = [[NeuronKohonen(self._learningRate, self._noOfInputs) for x in range(self._width)] for y in range(self._height) ]
    
    """Funkcja trenowania sieci"""
    def train(self, inputs):
        winner = self.guess(inputs)
        winner.train() #wagi zwycięzcy zostają uaktualnione

        return winner
    
    """Funkcja wyłaniająca najsilniejszy neuron"""
    def guess(self, inputs):
        lowestOutput = 10
        winner = (0,0)
        for i in range(self._height):       #wybierany zostaje neuron o najmniejszej odleglosci wektorow: wejscia od wag
            for j in range(self._width):
                tmp = self._neurons[i][j].guess(inputs)
                if tmp < lowestOutput:
                    lowestOutput = tmp
                    winner = (i, j)
                    
        return self._neurons[winner[0]][winner[1]]

    """Funkcja przywracająca początkowe wagi neuronów"""
    def resetNeurons(self):
        for i in range(self._height):
            for j in range(self._width):
                self._neurons[i][j].resetNeuron()
        