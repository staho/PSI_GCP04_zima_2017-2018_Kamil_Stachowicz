import Neuron
import SingleLayer
from testinput import *
from sign import *
from sigm import *
from signsigm import *
from MultiLayer import *
import numpy as np
np.random.seed(7)

if __name__ == '__main__':
    activation_function = SignSigm()(1.0)
    activation_function_der = SignSigm().derivative(1.0)

    activation_function1 = Sign()()
    activation_function_der1 = Sign().derivative()

    testInput = TestInput()
    testInputMap = testInput.getInputsMap()

    epochCnt = 10000
    hebbMultiLayer = MultiLayer(64, [1], [[activation_function, activation_function_der]], 0.007, 0.1)
    for i in range(0, epochCnt):
        for key in testInputMap.keys():
            if i % 100 == 0:
                print("Key:", key, end='')
                print(" =", hebbMultiLayer.trainNetwork(testInputMap[key]))
        if i % 100 == 0:
            print()

    #epochCnt = 10000
    #hebbMultiLayer = Neuron(0.007, 64, activation_function, activation_function_der, 0.1)
    #for i in range(0, epochCnt):
    #    for key in testInputMap.keys():
    #        if i % 100 == 0:
    #            print("Key:", key, end='')
    #            print(" =", hebbMultiLayer.trainWithoutSupervisor(testInputMap[key]))
    #    if i % 100 == 0:
    #        print()