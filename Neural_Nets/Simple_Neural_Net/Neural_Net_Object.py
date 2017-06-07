import numpy as np

class Neural_Network(object) :

    #Default Constructor - Input Space = 3, Output Space = 1, Hidden Nodes Space = 3
    def __init__(self):
        self.inputLayerSize = 3
        self.outputLayerSize = 1
        self.hiddenNodes = 3

        #Weights
        self.W_1 = np.random.randn(self.inputLayerSize, self.hiddenNodes)
        self.W_2 = np.random.randn(self.hiddenNodes, self.outputLayerSize)


    def forward(self, X) :
        #Propagate inputs through netowrks
        self.z_2 = np.dot(X, self.W_1)
        self.a_2 = self.sigmoid(self.z_2)
        self.z_3 = np.dot(self.a_2, self.W_2)
        yHat = self.sigmoid(self.z_3)
        return yHat



    def sigmoid(self, z) :
        return 1 / (1 + np.exp(-z))




