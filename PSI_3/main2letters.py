import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *
from multilayer import *
from testinput2 import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    test = TestInput2.makeTestInputs(16)


    multilayer = MultiLayer(35, [[activation_function, activation_function_der],
                                [activation_function, activation_function_der],
                                [activation_function, activation_function_der]],
                                [35,15,1], 0.1)

    inputData = []
    outputData = []
    for inp in test[0]:
        inputData.append(inp[0])

    for out in test[1]:
        outputData.append(out[0][0])

    lettersData = test[2]
    print(outputData)
    multilayer.trainNetwork(inputData, outputData)

    test = TestInput2.makeTestInputs(17)
    inputData = test[0]
    outputData = test[1]
    lettersData = test[2]

    for i in range(0, 17):
        print("Letter of test:", lettersData[i], "output", outputData[i][0])
        print(multilayer.guess(inputData[i][0]))
