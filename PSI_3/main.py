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
