Linear Regression Template 
------------

Available Functions
------------
__Regression(X, Y, lambda\_value)__ 
    
    - __X__ is the feature set 
    - __Y__ is the classification
    - __Lambda\_value__ is the regularizer 
    - Returns a vector __w__ that contains all the trained weights for each feature 
    - Returns a offset __b__ 

__Loss\_Function(X, Y, w, b)__
    
    - __X__ is the feature set 
    - __Y__ is the classification
    - __w__ is a vector of weights 
    - __b__ is the offset 
    - Fitness is based on the lowest square error
    - Returns a __L__ which is the square error of the function 

Sample Call: argv[1] = Data Set , argv[2] = Lambda Value

```bash
python3 Linear_Regression.py Data_Set/housing.data 0.001
```

Sample Ouput: 

'''bash

----- w -----
[[ -1.08005626e-01]
 [  4.64220587e-02]
 [  2.05100877e-02]
 [  2.68656088e+00]
 [ -1.77550976e+01]
 [  3.80995606e+00]
 [  6.81976275e-04]
 [ -1.47539719e+00]
 [  3.06022426e-01]
 [ -1.23355051e-02]
 [ -9.52619511e-01]
 [  9.31228383e-03]
 [ -5.24771088e-01]]
----- b -----
36.4513231627
----- l -----
21.8948315867

'''

Credit 
------------
Data Set = https://archive.ics.uci.edu/ml/datasets/housing
