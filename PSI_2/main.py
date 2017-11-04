import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *
from sign import *
from multilayer import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    activation_function1 = Sign()()
    activation_function_der1 = Sign().derivative()

    #def __init__(self, no_of_perceptrons, no_of_inputs, learning_rate, activation_function, activation_function_der):
    #singleLayer = SingleLayer(0, 3, 35, 0.5, activation_function, activation_function_der)
    #for i in range(0, 500):
    #    singleLayer.trainPercpeptrons(TestInput.makeTestInputs(10))

    multiLayer = MultiLayer(35, [[activation_function, activation_function_der],[activation_function1, activation_function_der1]], [3,1], 0.5)
    for i in range(0, 100):
        multiLayer.trainNetwork(TestInput.makeTestInputs(10))

    toGuess = TestInput.makeTestInputs(10)
    for inputs in toGuess:
        print("Letter: ", inputs._letterOfTest)
        x = multiLayer.guess(inputs._testArguments[0])
        if x[0] == 1:
            print("Capital\n")
        else:
            print("Small\n")
