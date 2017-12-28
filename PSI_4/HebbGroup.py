from Neuron import *

class HebbGroup:
    def __init__(self, learning_rate, no_of_neurons, no_of_inputs, forget_rate, activation_function):
        self._no_of_inputs = no_of_inputs
        self._no_of_neurons = no_of_neurons
        self._learning_rate = learning_rate
        self._forget_rate = forget_rate
        self._neurons = [ Neuron(x, self._learning_rate, self._no_of_inputs, activation_function, self._forget_rate) for x in range(self._no_of_neurons) ]

    def train_without_supervisor(self, input):
        winner = self._neurons[0]
        for neuron in self._neurons:
            temp_winner = neuron
            neuron.guess(input)
            if temp_winner._val > winner._val:
                winner = temp_winner
            
        winner.trainWithoutSupervisor(input)
        return winner

    def guess(self, input):
        winner = None
        for neuron in self._neurons:
            temp_winner = neuron
            neuron.guess(input)
            if winner == None:
                winner = neuron
            elif temp_winner._val > winner._val:
                winner = temp_winner
        
        return winner