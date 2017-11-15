import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *
from multilayer import *
from linear import *
from prettytable import PrettyTable

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    activation_function2 = Linear()(1.0)
    activation_function2_der = Linear().derivative(1.0)

    test = TestInput()
    test.makeTestInputs(1000)


    multilayer = MultiLayer(2,     [[activation_function, activation_function_der],
                                    [activation_function2, activation_function2_der]],
                                    [30,1], 0.01)


    multilayer.trainNetwork(test.getInputData(), test.getOutputData())

    test = TestInput()
    test.makeTestInputs(0.5)
inputs = test.getInputData()
outputs = test.getOutputData()

t = PrettyTable()
t.field_names = ['x1', 'x2', 'PREDICTED', 'EXPECTED']
for i in range(0, len(test.getInputData())):
    t.add_row([inputs[i][0], inputs[i][1], multilayer.guess(inputs[i])[0], outputs[i]])
print(t)
