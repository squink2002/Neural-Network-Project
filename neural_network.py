import numpy as np

class neural_network:

    class neuron:
        def __init__(self, weights, bias) -> None:
            # Initialize weights and bias randomly
            self.weights = np.random.randn()
            self.bias = np.random.randn() 

        """
        H = hidden layer
        Y = output layer
        W1 = weights 1 
        W2 = weight 2
        """
        def forward_propagate(self, X):
            # Hidden layer activation: 
            H = self.sigmoid(np.dot(X, self.W1))
            # Output layer activation:
            Y = self.sigmoid(np.dot(H, self.W2)) + self.bias
            return H, Y

        def back_propagate(self, X, H, Y, y_true):
            rows = X.shape[0]
            error = Y - y_true
            # Gradient for output layer weights:
            dW2 = (1/rows) * np.dot(H.T, error)
            # Backpropgating the error to the hidden layer: 
            dH = np.dot(error, self.W2.T) * self.sigmoid_derivative(H)
            # Gradient for hidden layer weights:
            dW1 = (1/rows) * np.dot(X.T, dH)
            return dW1, dW2

        """
        Initializing the Weight Values: The weights are initialized to the required neuron number at the input, hidden layer, and output. We initialize with random values.
        """
        def initialize_weights(self):
            # TODO
            return 

        """
        Updating the Weights: The weights are updated after each iteration using the learning rate value and the calculated derivative of the weights.
        """
        def update_weights(self):
            #TODO
            return
    
