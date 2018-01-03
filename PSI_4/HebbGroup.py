from Neuron import *

class HebbGroup:
    """Inicjalizacja sieci"""
    def __init__(self, learning_rate, no_of_neurons, no_of_inputs, forget_rate, activation_function):
        self._no_of_inputs = no_of_inputs
        self._no_of_neurons = no_of_neurons
        self._learning_rate = learning_rate
        self._forget_rate = forget_rate
        self._neurons = [ Neuron(x, self._learning_rate, self._no_of_inputs, activation_function, self._forget_rate) for x in range(self._no_of_neurons) ]

    """Funkcja trenowania bez nauczyciela"""
    def train_without_supervisor(self, inputs):
        winner = self._neurons[0]
        for neuron in self._neurons:    #wyszukanie neuronu o najwyzszym wyjsciu dla danego zestawu
            temp_winner = neuron
            neuron.guess(inputs)
            if temp_winner._val > winner._val:
                winner = temp_winner    #znalezenie neuronu 
            
        winner.trainWithoutSupervisor(inputs)   #aktualizacja wag neuronu
        return winner

    """Funkcja odgadywania"""
    def guess(self, inputs):
        winner = None       #wyszukanie neuronu o najwyzszym wyjsciu dla danego zestawu
        for neuron in self._neurons:
            temp_winner = neuron
            neuron.guess(inputs)s
            if winner == None:
                winner = neuron
            elif temp_winner._val > winner._val:
                winner = temp_winner
        
        return winner   #zwrócenie neuronu o najwyzszym wyjsciu