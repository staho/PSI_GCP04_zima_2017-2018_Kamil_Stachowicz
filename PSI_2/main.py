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

    tabOfLR = [0.01, 0.05, 0.1, 0.5]
    for lr in tabOfLR:
        print("LearningRate;",lr,';')
        multiLayer = MultiLayer(35, [[activation_function, activation_function_der],[activation_function1, activation_function_der1]], [3,1], lr)

        multiLayer.trainNetwork(TestInput.makeTestInputs(17))

        toGuess = TestInput.makeTestInputs(17)
        for inputs in toGuess:
            print("Letter;",inputs._letterOfTest,end='')
            x = multiLayer.guess(inputs._testArguments[0])
            if x[0] == 1:
                print(";1;")
            else:
                print(";0;")
