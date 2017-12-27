#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from HebbGroup import *
from testinput import *
from signsigm import *
import numpy as np
import copy
np.random.seed(7)

def drawEmoji(emoji):
    for i in range(8):
        for j in range(8):
            print(' ' if emoji[i*8+j] == -1 or emoji[i*8+j] == 0 else 'x', end=' ', flush=True)
        print("\n")

def noiseEmoji(emoji, numOfNoisePixels):
    
    noisedEmoji = copy.deepcopy(emoji)
    pixels = np.random.choice(64, numOfNoisePixels, replace=False)
    for pixel in pixels:
        noisedEmoji[pixel] *= -1

    return noisedEmoji
            

if __name__ == '__main__':
    learning_rate = 0.007
    forget_rate = 0.472
    activation_function = Linear()()


    testInput = TestInput()
    testInputMap = testInput.getInputsMap()
    noisedInputMap = {}
    
    for key in testInputMap.keys():
        noisedInputMap[key] = noiseEmoji(testInputMap[key], 2)

    for key in testInputMap.keys():
        print(str(key))
        drawEmoji(testInputMap[key])
        print("NOISED:")
        drawEmoji(noisedInputMap[key])
    
    epochCnt = 1000
    neuronGroup = HebbGroup(learning_rate, 100, 64, forget_rate, activation_function)

    winners = []
    for key in testInputMap.keys():
        winner = None
        for i in range(epochCnt):
            if winner == None:
                winner = neuronGroup.train_without_supervisor(testInputMap[key])
            else:
                winner = neuronGroup.train_without_supervisor(testInputMap[key])
        winners.append((key, winner))
    
    winnersNoised = {}
    for key in noisedInputMap.keys():
        winnersNoised[key] = neuronGroup.guess(noisedInputMap[key])
    
    for key, winner in winners:
        print(key, "\t", winner._iid, "\t", winnersNoised[key]._iid)
    