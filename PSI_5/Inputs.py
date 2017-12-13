import random
import numpy as np
import math

class Inputs:
    def __init__(self):
        self.__dict__['_inputs'] = {}
        self.__dict__['_species'] = None
        self._pathToData = './irisdata.txt'
        self._avgMap = {}
        
        self.readData()

        self.__dict__['_dataLen'] = len(self._inputs)

    def readData(self):
        with open(self._pathToData) as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                if line[4] is not self._inputs:
                    self._inputs.setdefault(line[4], []) 
                self._inputs[line[4]].append(self.normalize([float(i) for i in line[0:4]]))
        
        self._species = list(self._inputs.keys())
      
        self.averages()

    def getInputData(self, specie):
        if specie > -1 and specie < len(self._species):
            specieName = self._species[specie]

            index = random.randint(0, len(self._inputs[specieName]) - 1)
            return (specieName, self._inputs[specieName][index])
        else:
            return None
    
    def normalize(self, v1):
        sum = 0
        for x in v1:
            sum += x**2
        return [i/math.sqrt(sum) for i in v1]

    def averages(self):
        self._avgMap = {}
        for specie in self._species:
            x1 = 0
            x2 = 0
            x3 = 0
            x4 = 0
            for inp in self._inputs[specie]:
                x1 += inp[0]
                x2 += inp[1]
                x3 += inp[2]
                x4 += inp[3]
            lenght = len(self._inputs[specie])
            self._avgMap[specie] = ["{0:.2f}".format(x1/lenght), "{0:.2f}".format(x2/lenght), "{0:.2f}".format(x3/lenght), "{0:.2f}".format(x4/lenght)]
            print(specie,end=' ')
            print(self._avgMap[specie])
        print("--------------------------------------------------")
