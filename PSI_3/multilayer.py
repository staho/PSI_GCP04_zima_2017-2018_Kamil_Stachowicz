from perceptron import *
from singlelayer import *
from testinput import *

class MultiLayer():
    """docstring forMultiLayer."""
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

    def trainNetwork(self, inputs):
        for layer in self._perceptronLayersArray:
            layer.trainPercpeptrons(inputs)

    def guess(self, inputs):
        tempOutput = inputs
        for layer in self._perceptronLayersArray:
            tempOutput = layer.guess(tempOutput)

        return tempOutput
