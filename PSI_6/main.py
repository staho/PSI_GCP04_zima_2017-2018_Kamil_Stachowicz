from Grid import *
from testinput import *
from collections import Counter
import csv

if __name__ == '__main__':
    """Wstępna konfiguracja sieci"""
    gridn = 20
    gridm = 20
    epoch = 50
    for neighbourhoodMaxRay, neighbourhoodMinRay in [(3, 0.5), (5, 1), (20, 0.5)]:
        for learningRate in [0.1, 0.5, 0.01]:
            with open('results.csv', 'a', newline="") as csvfile:
                resultWriter = csv.writer(csvfile, dialect='excel')
                gridNxM = (gridn, gridm)
                resultWriter.writerow(['Lr'] + ['Epoch'] + ['GridDim'] + ['maxRay'] + ['minRay'])
                resultWriter.writerow([learningRate] + [epoch] + [gridNxM] + [neighbourhoodMaxRay] + [neighbourhoodMinRay])

                """Generowanie danych testowych"""
                testInputInstance = TestInput()
                testInputs = testInputInstance._testArguments
                noOfInputs = len(testInputs['A'])

                """Utworzenie siatki neuronów"""
                kohonenGrid = Grid(noOfInputs, learningRate, gridn, gridm, neighbourhoodMaxRay, neighbourhoodMinRay, epoch)

                """Trenowanie sieci"""
                winners = {}
                activeNeurons  = []
                for i in range(epoch):
                    for key, value in testInputs.items():
                        winners[key] = kohonenGrid.train(value, i)

                """Sprawdzenie liczby działających w sieci neuronów"""
                uniqueNeurons = len(Counter(winners.values()).keys())
                resultWriter.writerow(['Ilosc aktywnych'] + [uniqueNeurons])
                print("Ilosc aktywnych", str(uniqueNeurons))

                """Zaszumienie danych testowych"""
                noisedInput = []
                for i in range(7):
                    noisedInput.append(testInputInstance.getNoisedLetters(i))

                winnersTest = {}
                matched = Counter()
                almostMatched = Counter()
                badMatched = Counter()
                noisedCounter = 0

                resultWriter.writerow(['Ilosc zaszumionych'] + ['Ilosc idealnie'] + ['Ilosc w najwiekszym sasiedztwie'] + ['Ilosc blednych'])

                """Testowanie wyuczonej sieci"""
                for inputs in noisedInput:
                    for key, value in inputs.items():
                        tempWinner = kohonenGrid.guess(value)
                        if winners[key] == tempWinner:
                            matched[noisedCounter] += 1
                        elif winners[key].getDistanceToOther(tempWinner) <= 2:
                            almostMatched[noisedCounter] += 1
                        else:
                            badMatched[noisedCounter] += 1
                            print("Winner in training: ", winners[key].getNeuronString(), " winner in noised: ", tempWinner.getNeuronString(), " no of noised: ", noisedCounter)
                    resultWriter.writerow([noisedCounter] + [matched[noisedCounter]] + [almostMatched[noisedCounter]] + [badMatched[noisedCounter]])
                    noisedCounter += 1



                print("Exacly matched")
                print(matched)
                print("Almost matched")
                print(almostMatched)
