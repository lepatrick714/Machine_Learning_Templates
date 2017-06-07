import numpy as np

class Neural_Network(object) :
    def __init__(self) :
        #Define HyperParameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        #Weights ( Hidden Nodes )
        self.W_1 = np.random.randn(self.inputLayerSize, \
                                    self.hiddenLayerSize)
        self.W_2 = np.random.randn(self.hiddenLayerSize, \
                                    self.outputLayerSize)

    def forward(self, X) :
        #Propagate inputs through netowrks
        self.z_2 = np.dot(X, self.W_1)
        self.a_2 = self.sigmoid(self.z_2)
        self.z_3 = np.dot(self.a_2, self.W_2)
        yHat = self.sigmoid(self.z_3)
        return yHat


    def backward(self, temp) :
        hoihowih

    def cost_Function_Prime(self, X, y) :
        #Compute derivative with respect with W_1 and W_2
        self.yHat = self.forward(X)

        delta_3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z_3))
        dJdW2 = np.dot(self.a2.T, delta_3)

        delta_2 = np.dot(delta_3, self.W_2.T) * self.sigmoidPrime(self.z_2)
        dJdW1 = np.dot(X.T, delta_2)

        return { "dJdW_1" : dJdW1, "djdW_2" : dJdW2}


    def costFunctionPrime(self, X, y) :
        #Needs Implmenting




    #All Non Linear Functions Listed Below
    def sigmoid(self, z) :
        #Applies sigmoid function on value z
        return 1 / (1 + np.exp(-z))

    def sigmoidPrime(self, z):
        sigmoid(z)*(1 - sigmoid(z))





