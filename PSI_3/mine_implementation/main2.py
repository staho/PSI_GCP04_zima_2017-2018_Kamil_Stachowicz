import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *
from multilayer import *
from linear import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    activation_function2 = Linear()(1.0)
    activation_function2_der = Linear().derivative(1.0)

    test = TestInput()
    test.makeTestInputs(0.05)


    multilayer = MultiLayer(2,     [[activation_function, activation_function_der],
                                    [activation_function2, activation_function2_der]],
                                    [30,1], 0.1)


    multilayer.trainNetwork(test.getInputData(), test.getOutputData())

    test = TestInput()
    test.makeTestInputs(0.5)

    for i in test.getInputData():
        print("x:", i[0], " y: ", i[1])
        print(multilayer.guess(i))
