from perceptron import *
from singlelayer import *
from testinput import *

class MultiLayer():
	"""Multilayer defines how many inputs we have on first layer, how many perceptrons we have in each layer and
	provides the communication between layers"""

	def __init__(   self,
					no_of_inputs_first_layer,
					array_of_activation_functions,  #2D array of activation functions for every layer ([act, actDir], [act, actDir])
					array_of_number_of_perceptrons, #length of this arr is no of layers
					learning_rate
					):

		self.__dict__['_learningRate'] = learning_rate
		self.__dict__['_noFirstLayerInputs'] = no_of_inputs_first_layer
		self.__dict__['_arrayOfActivationFunctions'] = array_of_activation_functions
		self.__dict__['_noOfLayers'] = len(array_of_number_of_perceptrons)
		self.__dict__['_numberOfPerceptronsArray'] = array_of_number_of_perceptrons
		self.__dict__['_perceptronLayersArray'] = []
		self.__dict__['_arrayOfLayersOutputs'] = []

		self.createLayers()

	def createLayers(self):
		for i in range(0, self._noOfLayers):
			if i == 0:
				self._perceptronLayersArray.append(SingleLayer(
					i, #no of layer
					self._numberOfPerceptronsArray[i],
					self._noFirstLayerInputs,
					self._learningRate,
					self._arrayOfActivationFunctions[i][0],
					self._arrayOfActivationFunctions[i][1]
				))
			else:
				self._perceptronLayersArray.append(SingleLayer(
					i,
					self._numberOfPerceptronsArray[i],
					self._numberOfPerceptronsArray[i-1],    #that's beacouse next layer will have such many inputs as prev layer had outputs
															#it's BAD beacuse hidden layer can also have their independent inputs OR not
					self._learningRate,
					self._arrayOfActivationFunctions[i][0],
					self._arrayOfActivationFunctions[i][1]
				))

	def trainNetwork(self, inputData, desiredOutput):
		mse = 1
		epoch = 0
		inputDataLen = len(inputData)
		print("Data length:", inputDataLen)
		while mse > 0.2:
			mse = 0
			epoch += 1
			for counter in range(0, len(inputData)):

				previousOutput = inputData[counter]
				for layer in self._perceptronLayersArray:
					previousOutput = layer.guess(previousOutput)
					#print("Outputs:", previousOutput)

				previousError = []
				for i in range(self._noOfLayers -1, -1, -1):
					self._perceptronLayersArray[i].cleanErrorArray()
					if i == self._noOfLayers - 1:
						#print(desiredOutput[counter], previousOutput[0])               #calculate last error
						previousError.append(desiredOutput[counter] - previousOutput[0])
						mse += self.MSE(desiredOutput[counter], previousOutput[0])

					else:
						for x in range(0, self._perceptronLayersArray[i].getPerceptronNumer()): #x is also for next layer perceptron weights
							self._perceptronLayersArray[i].getErrorArray().append(0)
							for errorCounter in range(0, len(previousError)):
								dif = self._perceptronLayersArray[i+1].getPerceptron(errorCounter).getWeight(x)
								dif *= previousError[errorCounter]

								self._perceptronLayersArray[i].getErrorArray()[x] += dif
						previousError = self._perceptronLayersArray[i].getErrorArray()
						self._perceptronLayersArray[i].updateWeights()

			mse /= inputDataLen
			#if epoch % 10 == 0:
			print("Epoch: ", epoch, " mse: ", mse)
			#if epoch % 10 == 0:
				#print("Guessing x:", inputData[0][0], " x2: ", inputData[0][1], " wynik: ", self.guess(inputData[0]), "spodziewany: ", desiredOutput[0])


	def guess(self, inputs):
		tempOutput = inputs
		for layer in self._perceptronLayersArray:
			tempOutput = layer.guess(tempOutput)

		return tempOutput

	def MSE(self, result, expected):
		sum = 0
		#for i in range(len(result)):
		sum += (result - expected)**2
		return sum
