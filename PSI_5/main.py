from Grid import *
from Inputs import *
from NeuronKohonen import *

if __name__ == '__main__':
    #ustawienia i parametry sieci neuronowej
    learningRate = 1
    noOfInputs = 4
    width = 20
    height = 20

    inputs = Inputs()   #utworzenie danych wejściowych
    
    """Przypisanie danych róznych kwiatow to zmiennych"""
    species = {}
    for i in range(3):
        species[inputs.getInputData(i)[0]] = inputs.getInputData(i)[1]
    
    #zainicjalizowanie siatki neuronów Kohonena WTA
    grid = Grid(noOfInputs, learningRate, width, height)

    #tablica zwycięzców Kohonena
    winner = {}

    #wśród wszystkich neuronów w siatce odnajdywany jest zwycięzca
    for i in range(100):
        for j in range(len(species["Iris-setosa"])):
            for key in species.keys():
                winner[key] = grid.train(species[key][j])

    for key, value in winner.items():
        print(key + " " + value.getWeightsAsString())

    testData = {}
    for i in range(3):
        testData[inputs.getTestData(i)[0]] = inputs.getTestData(i)[1]

    #sprawdzanie jak wiele z danych testowych zostanie poprawnie odgadnięte
    matched = 0
    winnerTest = {}
    for key, value in testData.items():
        for j in range(len(testData["Iris-setosa"])):
            winnerTest[key] = grid.guess(value[j])
            if winnerTest[key] == winner[key]:
                matched += 1

    print(matched)
    """średnie z danych wejściowych"""
    #averages:
    #Iris-setosa [5.01, 3.42, 1.47, 0.25]
    #Iris-versicolor [5.94, 2.78, 4.26, 1.33]
    #Iris-virginica [6.59, 2.98, 5.56, 2.03]

    """średnie z danych znormalizowanych"""
    #averages:
    #[0.81, 0.55, 0.24, 0.04]
    #[0.75, 0.35, 0.54, 0.17]
    #[0.71, 0.32, 0.6, 0.22]
