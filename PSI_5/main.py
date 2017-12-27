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
    
    grid = Grid(noOfInputs, learningRate, 20, 20)

    winner = [None, None, None]

    for j in range(3):
        for i in range(1000):
            winner[j] = grid.train(inputs.getInputData(j)[1])
        grid.resetNeurons()

    print(specie + " " + winner[0].getWeightsAsString())
    print(specie1 + " " + winner[1].getWeightsAsString())
    print(specie2 + " " + winner[2].getWeightsAsString())

    #averages:
    #Iris-setosa [5.01, 3.42, 1.47, 0.25]
    #Iris-versicolor [5.94, 2.78, 4.26, 1.33]
    #Iris-virginica [6.59, 2.98, 5.56, 2.03]

    #averages:
    #[0.81, 0.55, 0.24, 0.04]
    #[0.75, 0.35, 0.54, 0.17]
    #[0.71, 0.32, 0.6, 0.22]
