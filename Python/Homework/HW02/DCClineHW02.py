# -*- coding: utf-8 -*-
"""
Your name: 
@author: DC Cline
"""
import pandas as pd

def main():
    df = pd.read_csv("HW02File.csv")    
    matrix = df.to_numpy()
    print("Number of rows: ", len(matrix))
    print("Number of columns: ", len(matrix[0]))
    print(matrix)
    
    print("Largest element: ", findLargest(matrix))    
    print("Row with lowest ratio: ", findLowestRatio(matrix, 1, 0))
    print("After scaling column 1")
    scaleColumn(matrix, 1, 2, 5)
    print(matrix)
    print("After scaling all columns")

    for i in range(len(matrix[0])):
        scaleColumn(matrix, i, 0, 1)
    print(matrix)
    print("")

"""
This function returns the largest element in the entire matrix
"""
def findLargest(matrix):
    largest = 0
    for i in matrix:
        for j in i:
            if j > largest:
                largest = j
    return largest

"""
This method returns the row with the lowest ratio between the first column specified by numCol and the second column specified by denCol
""" 
def findLowestRatio(matrix, numCol, denCol):
    lowestRatioNum = 999
    rowNum = 0
    for i in matrix:
        if i[numCol]/i[denCol] < lowestRatioNum:
            lowestRatioNum = i[numCol]/i[denCol]
            lowestRatio = rowNum
        rowNum += 1
    return lowestRatio

"""
This method scales the column in the matrix specified so that all the values in 
that column will fit the range such that the 
smallest value is equal to newMin and the largest is equal to newMax
"""
def scaleColumn(matrix, column, newMin, newMax):
    currentMin = 999
    currentMax = 0
    #set currentMin and currentMax
    for i in matrix:
        if i[column] < currentMin:
            currentMin = i[column]
        if i[column] > currentMax:
            currentMax = i[column]
    #scale column
    for i in matrix:
        i[column] = (i[column] - currentMin)/(currentMax - currentMin) * (newMax - newMin) + newMin
    return

main()