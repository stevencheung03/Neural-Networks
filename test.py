import unittest

from neuron import *

class TestNeuron(unittest.TestCase):
    def test_activation_sum_case_0(self):
        weights = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
        bias = 0.5
        delta = 0
        output = 0
        neuron = Neuron(weights, bias, delta, output)
        data_input = [2.78, 2.55, 2.78, 2.55, 2.78, 2.55, 2.78, 2.55]
        result = neuron.weighted_sum(data_input)
        self.assertEqual(result, 10.047999999999998)

    def test_activation_sum_case_1(self):
        weights = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
        bias = 0.5
        delta = 0
        output = 0
        neuron = Neuron(weights, bias, delta, output)
        data_input = [2.78, 2.55, 2.78, 2.55]
        result = neuron.weighted_sum(data_input)
        self.assertEqual(result, 10.047999999999998)

if __name__ == "__main__":
    unittest.main()
    