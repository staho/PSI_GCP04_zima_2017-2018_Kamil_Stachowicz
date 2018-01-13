from Grid import *
from testinput import *

if __name__ == '__main__':
    learningRate = 0.1
    gridNxM = (20, 20)
    neighbourhoodRay = 4
    epoch = 100

    testInputInstance = TestInput()
    testInputs = testInputInstance._testArguments
    noOfInputs = len(testInputs['A'])

    kohonenGrid = Grid(noOfInputs, learningRate, gridNxM[0], gridNxM[1], neighbourhoodRay)

    winners = {}
    for i in range(epoch):
        for key, value in testInputs.items():
            winners[key] = kohonenGrid.train(value)

    noisedInput = []
    for i in range(7):
        noisedInput.append(testInputInstance.getNoisedLetters(i))

    winnersTest = {}
    matched = 0
    for inputs in noisedInput:
        for key, value in inputs.items():
            tempWinner = kohonenGrid.guess(value)
            if winners[key] == tempWinner:
                matched += 1
            else:
                print("Winner in training: ", winners[key].getNeuronString(), " winner in noised: ", tempWinner.getNeuronString())



    print(matched)
