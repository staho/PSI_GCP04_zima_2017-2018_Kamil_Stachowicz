#!/usr/bin/python

from adaline import Adaline
from testinput import TestInput

class SingleLayer:


	def __init__(self, no_of_layer, no_of_perceptrons, no_of_inputs, learning_rate, typeOfAdaline):
		self.__dict__['_perceptrons'] = []
		self.__dict__['_testInputs'] = []
		self.__dict__['_perceptronOutputs'] = []
		self.__dict__['_noOfInputs'] = no_of_inputs
		self.__dict__['_learningRate'] = learning_rate
		self.__dict__['_noOfPerceptrons'] = no_of_perceptrons
		self.__dict__['_thisLayerNo'] = no_of_layer
		self.__dict__['_typeOfAdaline'] = typeOfAdaline

		for i in range(self._noOfPerceptrons):
			self._perceptrons.append(Adaline(self._learningRate, self._noOfInputs, self._typeOfAdaline))

	def getPerceptron(self, index_of_perceptron):
		if index_of_perceptron < 0 or index_of_perceptron >= len(self._perceptrons) :
			return None
		else:
			return self._perceptrons[index_of_perceptron]

	def trainPercpeptrons(self, inputs):

		for inp in inputs:
			perceptronCounter = 0
			print("Trained letter: ", inp._letterOfTest)
			for perc in self._perceptrons:
				perc.train(
					inp._testArguments[self._thisLayerNo],
					inp._testArguments[self._thisLayerNo + 1][perceptronCounter]
				)
				perceptronCounter += 1

	def guess(self, inputs):
		self._perceptronOutputs = []
		for perc in self._perceptrons:
			self._perceptronOutputs.append(perc.guess(inputs))

		return self._perceptronOutputs
