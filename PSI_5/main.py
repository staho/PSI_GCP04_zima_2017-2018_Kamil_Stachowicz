from Grid import *
from Inputs import *
from NeuronKohonen import *

if __name__ == '__main__':
    inputs = Inputs()
    
    specie = inputs.getInputData(0)[0]
    specie1 = inputs.getInputData(1)[0]
    specie2 = inputs.getInputData(2)[0]
    
    learningRate = 0.001
    noOfInputs = 4
    
    grid = Grid(noOfInputs, learningRate, 10, 10)
    grid1 = Grid(noOfInputs, learningRate, 10, 10)
    grid2 = Grid(noOfInputs, learningRate, 10, 10)
    
    for i in range(10000):
        winner = grid.train(inputs.getInputData(0)[1])
        winner1 = grid1.train(inputs.getInputData(1)[1])
        winner2 = grid2.train(inputs.getInputData(2)[1])

    print(specie + " " + winner.getWeightsAsString())
    print(specie1 + " " + winner1.getWeightsAsString())
    print(specie2 + " " + winner2.getWeightsAsString())