from Grid import *
from testinput import *
from collections import Counter

if __name__ == '__main__':
    learningRate = 0.1
    gridNxM = (20, 20)
    neighbourhoodMaxRay = 3
    neighbourhoodMinRay = 0.5

    epoch = 100

    testInputInstance = TestInput()
    testInputs = testInputInstance._testArguments
    noOfInputs = len(testInputs['A'])

    kohonenGrid = Grid(noOfInputs, learningRate, gridNxM[0], gridNxM[1], neighbourhoodMaxRay, neighbourhoodMinRay, epoch)

    winners = {}
    for i in range(epoch):
        for key, value in testInputs.items():
            winners[key] = kohonenGrid.train(value, i)

    for key, value in winners.items():
        for key1, value1 in winners.items():
            if key1 != key and value == value1:
                print("Zjebalem")

    noisedInput = []
    for i in range(7):
        noisedInput.append(testInputInstance.getNoisedLetters(i))

    winnersTest = {}
    matched = Counter()
    almostMatched = Counter()
    noisedCounter = 0

    for inputs in noisedInput:
        for key, value in inputs.items():
            tempWinner = kohonenGrid.guess(value)
            if winners[key] == tempWinner:
                matched[noisedCounter] += 1
            elif winners[key].getDistanceToOther(tempWinner) < neighbourhoodMaxRay:
                almostMatched[noisedCounter] += 1
            else:
                print("Winner in training: ", winners[key].getNeuronString(), " winner in noised: ", tempWinner.getNeuronString(), " no of noised: ", noisedCounter)
        noisedCounter += 1


    print("Exacly matched")
    print(matched)
    print("Almost matched")
    print(almostMatched)
