import pandas as pd
import numpy as np
import csv
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

def main():
    

    # Read in the data from a file
    trainingDF = pd.read_csv("HW14Training.csv")
    
    # store the number of columns as a variable
    numColumns = len(trainingDF.columns)
    # create a numpy array from the data set
    voteData = np.array(trainingDF)
    # get our attribute columns from the numpy array
    attColumns = np.array(voteData[:, 1:numColumns - 1])
    # get our class column from the numpy array
    classColumn = np.array(voteData[:, numColumns - 1])

    # create a decision tree object and fit
    dt = tree.DecisionTreeClassifier()
    dt.fit(attColumns, classColumn)
    
    # create a NB object and fit
    nb = GaussianNB()
    nb.fit(attColumns, classColumn)
    
    # create a KNN object
    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(attColumns, classColumn)
    
    
    # Read in the testing data
    testDF = pd.read_csv("HW14Testing.csv")
    numColumns = len(testDF.columns)
    testData = np.array(testDF)
    # get our attribute columns from the numpy array
    testAttColumns = np.array(testData[:, 1:numColumns - 1])
    # get our class column from the numpy array
    testClassColumn = np.array(testData[:, numColumns - 1])
    
    # run the test set through the classifiers
    dtPredict = dt.predict(testAttColumns)
    nbPredict = nb.predict(testAttColumns)
    knnPredict = knn.predict(testAttColumns)
    
    # accuracy, precision, and recall using sklearn methods
    # accuracy
    dtAcc = accuracy_score(testClassColumn, dtPredict)
    nbAcc = accuracy_score(testClassColumn, nbPredict)
    knnAcc = accuracy_score(testClassColumn, knnPredict)
    # precision
    dtPrecision = precision_score(testClassColumn, dtPredict)
    nbPrecision = precision_score(testClassColumn, nbPredict)
    knnPrecision = precision_score(testClassColumn, knnPredict)
    # recall
    dtRecall = recall_score(testClassColumn, dtPredict)
    nbRecall = recall_score(testClassColumn, nbPredict)
    knnRecall = recall_score(testClassColumn, knnPredict)
    
    # print accuracy, precision, and reall
    print("Decision Tree: accuracy", dtAcc, "precision", dtPrecision, "recall", dtRecall)
    print("Nieve Bayes: accuracy", nbAcc, "precision", nbPrecision, "recall", nbRecall)
    print("K Nearest Neighbors: accuracy", knnAcc, "precision", knnPrecision, "recall", knnRecall)
    
    # create array to convert to CSV
    output = [["ID", "DTPrediction", "NBPrediction", "KNNPrediction"]]
    for i in range(len(dtPredict)):
        output.append([testData[i, 0], dtPredict[i], nbPredict[i], knnPredict[i]])
    
    # write out to the CSV file
    with open("DClineHW14Results.csv", mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(output)

main()