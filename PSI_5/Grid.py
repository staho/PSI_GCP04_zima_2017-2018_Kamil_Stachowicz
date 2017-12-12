from NeuronKohonen import *

"""Class for Kohonen network"""
class Grid:
    def __init__(self, noOfInputs, learningRate, height, width):
        self.__dict__['_noOfInputs'] = noOfInputs
        self.__dict__['_learningRate'] = learningRate
        self.__dict__['_height'] = height
        self.__dict__['_width'] = width
        self.__dict__['_neurons'] = [[NeuronKohonen(self._learningRate, self._noOfInputs) for x in range(self._width)] for y in range(self._height) ]

    def train(self, inputs):
        highestOutput = 0
        winner = (0,0)

        for i in range(self._height):
            for j in range(self._width):
                
                tmp = self._neurons[i][j].guess(inputs)
                if tmp > highestOutput:
                    highestOutput = tmp
                    winner = (i, j)

        print("Winner: " + str(winner))
        self._neurons[winner[0]][winner[1]].train()
    
    def guess(self, inputs):
        for i in range(self._height):
            for j in range(self._width):
                
                tmp = self._neurons[i][j].guess(inputs)
                if tmp > highestOutput:
                    highestOutput = tmp
        
        return highestOutput
        