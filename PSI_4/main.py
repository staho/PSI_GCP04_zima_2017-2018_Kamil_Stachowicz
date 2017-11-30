import Neuron
import SingleLayer
from testinput import *
from sign import *
from sigm import *
from MultiLayer import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    activation_function1 = Sign()()
    activation_function_der1 = Sign().derivative()

    testInput = TestInput()
    testInputMap = testInput.getInputsMap()

    hebbMultiLayer = MultiLayer(64, [1], 
                        [[activation_function, activation_function_der]], 0.01, 0.003)
    for i in range(0, 1000):
        for key in testInputMap.keys():
            if i % 10 == 0:
                print("Key:", key, end='')
                print(" = ", hebbMultiLayer.trainNetwork(testInputMap[key]))
        if i % 10 == 0:
            print()
