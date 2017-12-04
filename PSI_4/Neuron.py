import random
from math import exp
from sigm import Sigm
from sign import Sign
import numpy as np
np.random.seed(7)

class Neuron:
    def __init__(self, learning_rate, no_of_inputs, activation_function, activation_function_der, forgetRate):
        self.__dict__['_no_of_inputs'] = no_of_inputs
        self.__dict__['_weights'] = []
        self.__dict__['_inputs'] = []
        self.__dict__['_learningRate'] = learning_rate
        self.__dict__['_activationFunction'] = activation_function
        self.__dict__['_activationFunctionDer'] = activation_function_der
        self.__dict__['_bias'] = -0.5
        self.__dict__['_forgetRate'] = forgetRate
        self.__dict__['_sum'] = None
        self.__dict__['_error'] = None

        for weight in range(0, self._no_of_inputs):
            #self._weights = np.array([np.random.uniform(-1, 1) for _ in range(self._no_of_inputs)])
            self._weights.append(np.random.uniform(-1, 1))
            #self._weights = [-0.8473834212520857, 0.5598375844802292, -0.123181537118213, 0.44693035566188244, 0.9559790239932053, 0.07699174082086735, 0.002240927319875796, -0.8558977332804769, -0.46312203979625766, -0.00023499834888007776, 0.35845999224188096, 0.6074780722087509, -0.23811773370292322, -0.8681273061881898, -0.4237088013840129, 0.8191870554392273, -0.573229292840169, -0.09575207636463379, 0.8624120393780434, -0.950201544899304, 0.20109783492824507, 0.9002590008272913, -0.5393942419580704, 0.09697983847206082, 0.8182567497734625, -0.7336611084814997, 0.046825161347531674, 0.5008197182040697, 0.33802648176782757, -0.06449428051003858, -0.5903018194044098, -0.01846822181785912, -0.25523062122988205, -0.04519769029682319, -0.2682192284388141, 0.6758359886185212, 0.5372950130390186, -0.37201064557467567, 0.14525066528790798, -0.4479019033386098, -0.0943141349071992, -0.2940432681112106, 0.3147989255595165, -0.2592978340239296, -0.08181404421713712, 0.4386482450180831, -0.17401634177233083, 0.8128465383286774, -0.6390967615946368, 0.48223774582652856, -0.1552519127137193, -0.14709285463011534, 0.26875973726767755, 0.04581240205669057, -0.17022804312111361, -0.9971462388744836, -0.8154753083064958, 0.41878878745042547, 0.04869119353039442, 0.39232092703393784, 0.9109366460058519, 0.36582770875083503, -0.8937426186540849, -0.38229463027240573]
        if self._forgetRate == None:
            self._forgetRate = 0

    def guess(self, inputs):
        self._inputs = inputs

        self._sum = np.dot(self._weights, self._inputs) + self._bias

        return self._activationFunction(self._sum)

    def trainWithSupervisor(self, inputs, desiredOutput):  #∂wij(k+1) = (1-fr)*∂wij(k) + lr*yj*yi (yj to wejście nr j) yi to oczekiwane wyjscie
        output = self.guess(inputs)

        for i in range(len(self._inputs)):           
            self._weights[i] = (1-self._forgetRate) * self._weights[i] + self._learningRate * self._inputs[i] * desiredOutput

    def trainWithoutSupervisor(self, inputs): #∂wij(k+1) = (1-fr)*∂wij(k) + lr*yj*yi (yj to wejście nr j) yi to wyjście neuronu
        output = self.guess(inputs)

        constant = self._learningRate * output
        forget = (1-self._forgetRate)
        for i in range(len(self._inputs)):           
            self._weights[i] *= forget
            self._weights[i] += constant * self._inputs[i]
        
        return output
