import Neuron

"""Class for Kohonen network""""
class Grid:
    def __init__(self, noOfInputs, learningRate, height, width, activationFunction):
        self.__dict__['_noOfInputs'] = noOfInputs
        self.__dict__['_learningRate'] = learningRate
        self.__dict__['_height'] = height
        self.__dict__['_width'] = width
        self.__dict__['_activationFunction'] = activationFunction