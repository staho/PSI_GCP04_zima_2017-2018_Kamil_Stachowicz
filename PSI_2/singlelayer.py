#!/usr/bin/python

from perceptron import Perceptron
from testinput import TestInput

class SingleLayer:


	def __init__(self, no_of_layer, no_of_perceptrons, no_of_inputs, learning_rate, activation_function, activation_function_der):
		self.__dict__['_perceptrons'] = []
		self.__dict__['_testInputs'] = []
		self.__dict__['_perceptronOutputs'] = []
		self.__dict__['_activationFunction'] = activation_function
		self.__dict__['_activationFunctionDer'] = activation_function_der
		self.__dict__['_noOfInputs'] = no_of_inputs
		self.__dict__['_learningRate'] = learning_rate
		self.__dict__['_noOfPerceptrons'] = no_of_perceptrons
		self.__dict__['_thisLayerNo'] = no_of_layer

		for i in range(self._noOfPerceptrons):
			self._perceptrons.append(Perceptron(self._learningRate, self._noOfInputs, self._activationFunction, self._activationFunctionDer))

	def getPerceptron(self, index_of_perceptron):
		if index_of_perceptron < 0 or index_of_perceptron >= len(self._perceptrons) :
			return None
		else:
			return self._perceptrons[index_of_perceptron]

	def trainPercpeptrons(self, inputs):
		if(self._thisLayerNo != 0):
			for x in range(0, 200):
				for inp in inputs:
					perceptronCounter = 0

					for perc in self._perceptrons:
						perc.train(
							inp._testArguments[self._thisLayerNo],
							inp._testArguments[self._thisLayerNo + 1][perceptronCounter]
						)
						perceptronCounter += 1

		mse = 1;
		epoch = 0
		while(mse > 0.001):
			epoch += 1
			print("Epoch;",epoch,";",end='')
			for inp in inputs:
				perceptronCounter = 0

				outputs = []
				for perc in self._perceptrons:
					outputs.append(perc.train(
						inp._testArguments[self._thisLayerNo],
						inp._testArguments[self._thisLayerNo + 1][perceptronCounter]
					))
					perceptronCounter += 1
				mse+= self.MSE(outputs,inp._testArguments[self._thisLayerNo + 1])
			mse = mse/len(inputs)
			print("MSE;",mse,";")

	def guess(self, inputs):
		self._perceptronOutputs = []
		for perc in self._perceptrons:
			self._perceptronOutputs.append(perc.guess(inputs))

		return self._perceptronOutputs
	#Mean squared error
	def MSE(self, result, expected):
		sum = 0
		for i in range(len(result)):
			sum += (result[i] - expected[i])**2
		return sum
