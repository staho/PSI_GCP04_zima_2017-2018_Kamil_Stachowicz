import random
import numpy as np

class Inputs:
    def __init__(self):
        self.__dict__['_inputs'] = {}
        self.__dict__['_species'] = None
        self._pathToData = './irisdata.txt'
        
        self.readData()

        self.__dict__['_dataLen'] = len(self._inputs)

    def readData(self):
        with open(self._pathToData) as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                if line[4] is not self._inputs:
                    self._inputs.setdefault(line[4], []) 
                self._inputs[line[4]].append([float(i) for i in line[0:4]])
        
        self._species = list(self._inputs.keys())
      
    def getInputData(self, specie):
        if specie > -1 and specie < len(self._species):
            specieName = self._species[specie]

            index = random.randint(0, len(self._inputs[specieName]) - 1)
            return (specieName, self._inputs[specieName][index])
        else:
            return None