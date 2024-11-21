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
    
    # create array of chosen class based on majority voting
    majorityPredict = []
    for i in range(len(dtPredict)):
        # if two 1's found, append 1, else append 0
        if(dtPredict[i] + nbPredict[i] + knnPredict[i] >=2):
            majorityPredict.append(1)
        else:
            majorityPredict.append(0)
    
    # calculate accuracy, precision, and recall using sklearn methods
    # accuracy
    dtAcc = accuracy_score(testClassColumn, dtPredict)
    nbAcc = accuracy_score(testClassColumn, nbPredict)
    knnAcc = accuracy_score(testClassColumn, knnPredict)
    majorityAcc = accuracy_score(testClassColumn, majorityPredict)
    # precision
    dtPrecision = precision_score(testClassColumn, dtPredict)
    nbPrecision = precision_score(testClassColumn, nbPredict)
    knnPrecision = precision_score(testClassColumn, knnPredict)
    majorityPrecision = precision_score(testClassColumn, majorityPredict)
    # recall
    dtRecall = recall_score(testClassColumn, dtPredict)
    nbRecall = recall_score(testClassColumn, nbPredict)
    knnRecall = recall_score(testClassColumn, knnPredict)
    majorityRecall = recall_score(testClassColumn, majorityPredict)
    
    # print accuracy, precision, and recall for the 3 classifiers and the majority votes.
    print("Decision Tree: \nAccuracy:", dtAcc, "\nPrecision:", dtPrecision, "\nRecall:", dtRecall,)
    print("Nieve Bayes: \nAccuracy:", nbAcc, "\nPrecision:", nbPrecision, "\nRecall:", nbRecall)
    print("K Nearest Neighbors: \nAccuracy:", knnAcc, "\nPrecision:", knnPrecision, "\nRecall:", knnRecall)
    print("Majority: \nAccuracy:", majorityAcc, "\nPrecision:", majorityPrecision, "\nRecall:", majorityRecall)

    # create array to convert to CSV
    output = [["ID", "DT", "NB", "KNN", "Hybrid"]]
    for i in range(len(dtPredict)):
        output.append([testData[i, 0], dtPredict[i], nbPredict[i], knnPredict[i], majorityPredict[i]])
    
    # write out to the CSV file
    with open("DClineHW14Results.csv", mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(output)

# end of main

main()