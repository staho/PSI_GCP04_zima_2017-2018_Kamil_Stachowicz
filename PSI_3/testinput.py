#!/usr/bin/python
from equation import *

class TestInput():
    """
        Test input is a table of 2 vars and desired output from Rastrign 3D function
    """
    def __init__(self):
        self.__dict__['_inputData'] = []
        self.__dict__['_outputData'] = []
        #self.__dict__['_output'] = 1

    def makeTestInputs(self, dif):
        i = -2
        j = -2
        while i <= 2:
            while j <= 2:
                self._inputData.append([i, j])
                j += dif
            j = 0
            i += dif

        for data in self._inputData:
            self._outputData.append(Equation.getValue(data[0], data[1]))

    def getInputData(self):
        return self._inputData

    def getOutputData(self):
        return self._outputData
