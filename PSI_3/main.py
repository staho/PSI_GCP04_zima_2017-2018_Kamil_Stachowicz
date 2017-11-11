import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *
from multilayer import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    test = TestInput()
    test.makeTestInputs(0.5)

    multilayer = MultiLayer(2, [[activation_function,activation_function_der]], [2,2,1], 0.1)

    inputData = test.getInputData()
    outputData = test.getOutputData()

    for i in range(0, len(inputData)):
        multilayer.trainNetwork(inputData[i], outputData[i])
