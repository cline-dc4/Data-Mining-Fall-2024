# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:29:15 2024

@author: DThomas
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:59:13 2024

@author: DThomas
"""

import pandas as pd
import numpy as np
from sklearn import tree


def main():
    df = pd.read_csv("ContactsData.csv")    
    print(df.columns)
    print("Before dropping")
    print(df)
    numColumns = len(df.columns)
    print("Number of columns: ", numColumns)
    print(df)
    
    # replace contacts attribute
    df["Contacts"].replace(["hard","soft","none"],[0, 1, 2], inplace=True)
    print(df)
    
    #replace age attribute with dummy variable
    age = pd.get_dummies(df["Age"], drop_first=True, dtype=int)
    df.drop("Age", axis=1, inplace=True)
    
    #replace GlassType attribute
    glass = pd.get_dummies(df["GlassType"], drop_first=True, dtype=int)
    df.drop("GlassType", axis=1, inplace=True)
    
    #replace Astigmatism attribute
    astigmatism = pd.get_dummies(df["Astigmatism"], drop_first=True, dtype=int)
    df.drop("Astigmatism", axis=1, inplace=True)
    
    #replace TearProduction
    tear = pd.get_dummies(df["TearProduction"], drop_first=True, dtype=int)
    df.drop("TearProduction", axis=1, inplace=True)
    
    #Concatenate age, Glasstype, Astigmatism, TearProduction
    df = pd.concat([age, glass, astigmatism, tear, df], axis=1)
    print(df)
    
    attAndClass = np.array(df)
    attColumns = np.array(attAndClass[:, :len(df.columns)-1])
    classColumn = np.array(attAndClass[:, len(df.columns)-1])
    
    # Decision trees
    decision = tree.DecisionTreeClassifier()
    decision = decision.fit(attColumns, classColumn)
    tree.plot_tree(decision)
    

main()

