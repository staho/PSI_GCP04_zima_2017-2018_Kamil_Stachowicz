from Grid import *
from Inputs import *

if __name__ == '__main__':
    inputs = Inputs()

    learningRate = 0.01
    noOfInputs = 4
    
    grid = Grid(noOfInputs, learningRate, 10, 10)
    for i in range(1000):
        grid.train(inputs.getInputData()[1])
