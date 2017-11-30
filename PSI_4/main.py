import Neuron
import SingleLayer
from TestInput import *
from sign import *
from sigm import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derivative(1.0)

    activation_function1 = Sign()()
    activation_function_der1 = Sign().derivative()

    testInput = TestInput()
    testInputMap = testInput.getInputsMap()

    
