import numpy as np
from adaline import *
from testinput import *
from singlelayer import *
from multilayer import *

if __name__ == '__main__':
    multiLayer = MultiLayer(35, [3,1], 0.05, Adaline.AdalineType.MAJORITY)
    for i in range(0, 30):
        multiLayer.trainNetwork(TestInput.makeTestInputs(7))

    toGuess = TestInput.makeTestInputs(8)
    for inputs in toGuess:
        print("Letter: ", inputs._letterOfTest)
        x = multiLayer.guess(inputs._testArguments[0])
        if x[0] == 1:
            print("Capital\n")
        else:
            print("Small\n")
