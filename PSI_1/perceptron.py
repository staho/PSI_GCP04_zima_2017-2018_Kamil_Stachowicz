#!/usr/bin/python
import random

class Perceptron:

    def __init__(self, lr):
        self.weights = [0,0,0]
        self.weights[0] = random.uniform(-1,1)
        self.weights[1] = random.uniform(-1,1)
        self.weights[2] = random.uniform(-1,1)
        self.wrong = 0

        self.x = 0
        self.y = 0

        self.bias = 1
        self.learningRate = lr
        print("Learning rate = ", self.learningRate)
    def displayOutput(self):
        if self.x == -1:
            first = "false"
        else:
            first = "true"

        if self.y == -1:
            second = "false"
        else:
            second = "true"

        if self.output == 1:
            third = "true"
        else:
            third = "false"
        print("The output from: ", first, " and: ", second, " is: ", third)
        if self.x == -1:
            self.xbool = 0
        else:
            self.xbool = 1

        if self.y == -1:
            self.ybool = 0
        else:
            self.ybool = 1

        if self.output == -1:
            self.obool = 0
        else:
            self.obool = 1

        if self.xbool and self.ybool:
            if self.obool == 0:
                print("X")
                self.wrong += 1
        if (self.xbool and self.ybool) != 1:
            if self.obool == 1:
                print("X")
                self.wrong += 1

    def guess(self, x, y):
        self.x = x
        self.y = y
        self.output = x*self.weights[0] + y*self.weights[1] + self.bias*self.weights[2]
        if self.output >= 0:
            self.output = 1
        else:
            self.output = -1

        self.displayOutput()
        return self.output

    def train(self, x, y, desiredOutput):
        output = self.guess(x, y)
        error = desiredOutput - output

        self.weights[0] += error * self.x * self.learningRate
        self.weights[1] += error * self.y * self.learningRate
        self.weights[2] += error * self.bias * self.learningRate
