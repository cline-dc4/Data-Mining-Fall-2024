# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:37:54 2024

@author: DThomas
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():
    attAndClass=np.array([[  9.77075874,   3.27621022, 1],
       [ -9.71349666,  11.27451802, 2],
       [ -6.91330582,  -9.34755911, 1],
       [-10.86185913, -10.75063497, 1],
       [ -8.50038027,  -4.54370383, 2]])
    
    attColumns = np.array(attAndClass[:, 0:2])
    classColumn = np.array(attAndClass[:, 2])
    
    # creating he logistic regression model
    model = LogisticRegression(solver="liblinear", random_state=0)
    # fit the model to our data
    model.fit(attColumns, classColumn)
    print("b:", model.intercept_)
    print("m:", model.coef_)
    
    testPoints = np.array([[5, 5], [-9, 9]])
    
    # predictions for our test points
    predictions = model.predict(testPoints)
    print(predictions)
    
    
    values=np.array([[0.5, 0],
        [0.75, 0],
        [1, 0],
        [1.25, 0],
        [1.5,0],
        [1.75,0],
        [2,0],
        [2.25,0],
        [2.5,0],
        [2.75,1],
        [3,0],
        [3.25,0],
        [3.5,0],
        [4,1],
        [4.25,1],
        [4.5,1],
        [4.75,1],
        [5,1],
        [5.25,1]])
    attributes = np.array(values[:, 0])
    attributes = attributes.reshape(-1, 1)
    classes = np.array(values[:, 1])
    
main()










