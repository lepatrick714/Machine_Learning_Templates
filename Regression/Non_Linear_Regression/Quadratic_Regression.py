import sys
import time
#import csv
import numpy as np
from numpy.linalg import inv

def Regression(X, Y, lambda_value) :

    ''' Adding the columns of Ones '''
    col_Ones = np.ones((len(X), 1))
    X = np.append(col_Ones, X, 1)

    I = np.identity(len(X[0]))
    #print(len(I))
    I[0][0] = 0

    temp_1 = np.dot(np.transpose(X), X)
    temp_2 = lambda_value*I
    temp_3 = np.dot(np.transpose(X), Y)

    w = np.dot(inv(temp_1 + temp_2), temp_3)
    b = w[0][0]
    w = np.delete(w, (0), axis=0)
    return {'w': w, 'b': b}


def Loss_Function(X, Y, w, b) :
    L = 0

    temp_1 = np.dot(X, w)
    total = 0

    for i in range(0, len(X)) :
        ele = temp_1[i][0]
        curr = ele+b
        curr = (Y[i][0] - curr)
        curr = curr * curr
        total = total + curr

    L = total / len(X)
    return {'L': L}

def Quadratic_Function(X) :
    X_Quad = X
    for i in range(len(X[0])) :
        for j in range(i, len(X[0])) :

            '''print("Right Hand")
            print(len(X[:, i]*X[:, j]))

            print("Left Hand")
            print(len(X))
            print(i)
            print(len(X[:,i]))
            print(len(X[:,j]))
            print(len(X[:, i]*X[:, j]))
            '''

            temp = np.multiply(X[:, i],X[:, j])
            temp = np.reshape( temp,(-1,1) )
            #print("X_Quad {} Result {}".format(X_Quad.shape, temp.shape))
            X_Quad = np.append( X_Quad, temp , 1)

    #print(X.shape)
    #print("\n\n\n")
    #print(X_Quad.shape)
    return {'X_Quad' : X_Quad}


''' Loading the data and slicing it to X and Y componenets '''
data = np.loadtxt(sys.argv[1])

X = data[:,:len(data[0])-1]
Y = data[:, len(data[0])-1:]

''' Splitting the data up '''
X = data[:,:len(data[0])-1] #Data
Y = data[:, len(data[0])-1:] #Class

X_train = X[0: int(.80*len(X)), :]
Y_train = Y[0: int(.80*len(Y)), :]

X_test = X[int(.80*len(X))+1 : len(X)+1,:]
Y_test = Y[int(.80*len(Y))+1 : len(Y)+1,:]


''' Start Timer '''
start = time.time()
''' Start Timer '''

X_train = Quadratic_Function(X_train)
X_test = Quadratic_Function(X_test)
Regression_Result = Regression(X_train['X_Quad'], Y_train, float(sys.argv[2]))
Loss_Result = Loss_Function(X_test['X_Quad'], Y_test, Regression_Result["w"], Regression_Result["b"])

''' End Timer '''
elapsed = time.time()
''' End Timer '''


''' Outputs '''
print("--- Running Linear Regression ---")
print("--- Last updated June 8th, 2017 ---")
print("--- By Patrick Le @ lepatrick714 ---")

print("\n\n")

print("---- WEIGHTS ----")
print(Regression_Result["w"])

print("\n\n")

print("---- OFFSET ----")
print(Regression_Result["b"])

print("\n\n")

print("---- ACCURACY ---")
print("{} % Correct".format( 1*(100 - Loss_Result["L"]) ))

print("\n\n")

print("---- INACCURACY ----")
print("{} % Incorrect".format(Loss_Result["L"]))
print("\n\n")


print("--- END OF PROGRAM ---")

