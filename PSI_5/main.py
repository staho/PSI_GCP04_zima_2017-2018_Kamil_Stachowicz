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

    winner = [None, None, None]

    for j in range(3):
        for i in range(10000):
            winner[j] = grid.train(inputs.getInputData(j)[1])
        grid.resetNeurons()

    print(specie + " " + winner[0].getWeightsAsString())
    print(specie1 + " " + winner[1].getWeightsAsString())
    print(specie2 + " " + winner[2].getWeightsAsString())