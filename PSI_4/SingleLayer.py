
from Neuron import *
import testinput

class SingleLayer:


	def __init__(self, no_of_layer, no_of_perceptrons, no_of_inputs, learning_rate, forget_rate, activation_function, activation_function_der):
		self.__dict__['_perceptrons'] = []
		self.__dict__['_testInputs'] = []
		self.__dict__['_perceptronOutputs'] = []
		self.__dict__['_activationFunction'] = activation_function
		self.__dict__['_activationFunctionDer'] = activation_function_der
		self.__dict__['_noOfInputs'] = no_of_inputs
		self.__dict__['_learningRate'] = learning_rate
		self.__dict__['_noOfPerceptrons'] = no_of_perceptrons
		self.__dict__['_thisLayerNo'] = no_of_layer
		self.__dict__['_forgetRate'] = forget_rate

		for i in range(self._noOfPerceptrons):
			self._perceptrons.append(Neuron(self._learningRate, self._noOfInputs, self._activationFunction, self._activationFunctionDer, self._forgetRate))

	def getPerceptron(self, index_of_perceptron):
		if index_of_perceptron < 0 or index_of_perceptron >= len(self._perceptrons) :
			return None
		else:
			return self._perceptrons[index_of_perceptron]

	def trainPercpeptrons(self, inputs):
		trainOutputs = []
		for neuron in self._perceptrons:
			trainOutputs.append(neuron.trainWithoutSupervisor(inputs))
		return trainOutputs

	def guess(self, inputs):
		self._perceptronOutputs = []
		for perc in self._perceptrons:
			self._perceptronOutputs.append(perc.guess(inputs))

		return self._perceptronOutputs
