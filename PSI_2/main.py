import numpy as np
from sigm import *
from perceptron import *
from testinput import *
from singlelayer import *

if __name__ == '__main__':
    activation_function = Sigm()(1.0)
    activation_function_der = Sigm().derative(1.0)

    #def __init__(self, no_of_perceptrons, no_of_inputs, learning_rate, activation_function, activation_function_der):
    singleLayer = SingleLayer(3, 35, 0.5, activation_function, activation_function_der)
