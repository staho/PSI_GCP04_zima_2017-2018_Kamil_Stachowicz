from HebbGroup import *
from testinput import *
from signsigm import *
import numpy as np
import copy

"""Funkcja drukująca emoji na ekran"""
def drawEmoji(emoji):
    for i in range(8):
        for j in range(8):
            print('⬛️' if emoji[i*8+j] == -1 or emoji[i*8+j] == 0 else '⬜️', end=' ', flush=True)
        print("\n")

"""Funkcja zaszumiająca losowe piksele w emoji"""
def noiseEmoji(emoji, numOfNoisePixels):
    noisedEmoji = copy.deepcopy(emoji)
    pixels = np.random.choice(64, numOfNoisePixels, replace=False)
    for pixel in pixels:
        if noisedEmoji[pixel] == 1:
            noisedEmoji[pixel] = 0
        else:
            noisedEmoji[pixel] = 1

    return noisedEmoji


if __name__ == '__main__':
    #ustawienie parametrów sieci i uczenia
    no_of_inputs = 64
    learning_rate = 0.008
    forget_rate = 0.25
    num_of_neurons = 30
    epochCnt = 400


    activation_function = Linear()()    #ustawienie funkcji aktywacji dla neuronów
    testInput = TestInput()             #wygenerowanie danych do uczenia
    testInputMap = testInput.getInputsMap()
    noisedInputMap = {}

    for key in testInputMap.keys():     #stworzenie zaszumionych emotikon do testów
        noisedInputMap[key] = noiseEmoji(testInputMap[key], 3)

    for key in testInputMap.keys():     #wydruk emoji
        print(str(key))
        drawEmoji(testInputMap[key])
        print("NOISED:")
        drawEmoji(noisedInputMap[key])

    #stworzenie struktury sieci Hebba
    neuronGroup = HebbGroup(learning_rate, num_of_neurons, no_of_inputs, forget_rate, activation_function)

    #uczenie sieci
    for i in range(epochCnt):
        for key in testInputMap.keys():
            neuronGroup.train_without_supervisor(testInputMap[key])

    #sprawdzenie sieci
    winners = {}
    for key in testInputMap.keys():
        winners[key] = neuronGroup.guess(testInputMap[key])

    #sprawdzenie sieci zaszumionymi emoji
    winnersNoised = {}
    for key in noisedInputMap.keys():
        winnersNoised[key] = neuronGroup.guess(noisedInputMap[key])

    #wydruki końcowe
    print("Emoji", "\t", "Norm", "\t", "Noised")
    print("-----------------------")
    for key, winner in winners.items():
        print(key, "\t", winner._iid, "\t", winnersNoised[key]._iid)
