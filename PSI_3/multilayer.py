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
                    self._arrayOfActivationFunctions[0][0],
                    self._arrayOfActivationFunctions[0][1]
                ))
            else:
                self._perceptronLayersArray.append(SingleLayer(
                    i,
                    self._numberOfPerceptronsArray[i],
                    self._numberOfPerceptronsArray[i-1],    #that's beacouse next layer will have such many inputs as prev layer had outputs
                                                            #it's BAD beacuse hidden layer can also have their independent inputs OR not
                    self._learningRate,
                    self._arrayOfActivationFunctions[0][0],
                    self._arrayOfActivationFunctions[0][1]
                ))

    def trainNetwork(self, inputs, desiredOutput):
        previousOutput = inputs
        for layer in self._perceptronLayersArray:
            previousOutput = layer.guess(previousOutput)

        previousError = []
        for i in range(self._noOfLayers -1, -1, -1):
            self._perceptronLayersArray[i].cleanErrorArray()
            print(i)
            if i == self._noOfLayers - 1:
                print(desiredOutput, previousOutput[0])               #calculate last error
                previousError.append(desiredOutput - previousOutput[0])
                print("Error on the end:", previousError)

            else:
                for x in range(0, self._perceptronLayersArray[i].getPerceptronNumer()): #x is also for next layer perceptron weights
                    self._perceptronLayersArray[i].getErrorArray().append(0)
                    print("Error in loop", previousError)
                    for errorCounter in range(0, len(previousError)):
                        dif = self._perceptronLayersArray[i+1].getPerceptron(errorCounter).getWeight(x)
                        dif *= previousError[errorCounter]

                        self._perceptronLayersArray[i].getErrorArray()[x] += dif
                previousError = self._perceptronLayersArray[i].getErrorArray()
                self._perceptronLayersArray[i].updateWeights()



    def guess(self, inputs):
        tempOutput = inputs
        for layer in self._perceptronLayersArray:
            tempOutput = layer.guess(tempOutput)

        return tempOutput
