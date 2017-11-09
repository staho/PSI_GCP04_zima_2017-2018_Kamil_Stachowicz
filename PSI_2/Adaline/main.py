import numpy as np
from adaline import *
from testinput import *
from singlelayer import *
from multilayer import *

if __name__ == '__main__':
    multiLayer = MultiLayer(35, [3,1], 0.05, Adaline.AdalineType.MAJORITY)
    tabOfLR = [0.01, 0.05, 0.1, 0.5]
    for lr in tabOfLR:
        print("LearningRate;",lr,';')
        multiLayer.trainNetwork(TestInput.makeTestInputs(17))

        toGuess = TestInput.makeTestInputs(17)
        for inputs in toGuess:
            print("Letter;",inputs._letterOfTest,end='')
            x = multiLayer.guess(inputs._testArguments[0])
            if x[0] == 1:
                print(";1;")
            else:
                print(";0;")
