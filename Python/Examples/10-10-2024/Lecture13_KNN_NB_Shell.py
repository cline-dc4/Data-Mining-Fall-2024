import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def main():
    attAndClass=np.array(
      [[  9.77075874,   3.27621022, 1],
       [ -9.71349666,  11.27451802, 0],
       [ -6.91330582,  -9.34755911, 1],
       [-10.86185913, -10.75063497, 1],
       [ -8.50038027,  -4.54370383, 0]])
    
    attColumns = np.array(attAndClass[:, 0:2])
    classColumn = np.array(attAndClass[:, 2])
    
    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(attColumns, classColumn)
    # test points to classify
    testPoints = [[5,3], [9,9], [-6,-10]]
    
    predictions = knn.predict(testPoints)
    print(predictions)
    
    # NB classifier
    nb = GaussianNB()
    nb.fit(attColumns, classColumn)
    
    predictions = nb.predict(testPoints)
    print(predictions)
    
    # Read in the data from a file
    df = pd.read_csv("ContactsDataNumbers.csv")
    print(df.columns)
    
    # store the number of rows and columns in variables
    numRows = len(df)
    numColumns = len(df.columns)
    # Creating a NB classifier
    # create a numpy array from the data set
    contactLensDS = np.array(df)
    # get our attribute columns from the numpy array
    # start at column 1 because our first column in the CSV is just an ID.
    attColumns = np.array(contactLensDS[:, 1:numColumns - 1])
    # get our class column from the numpy array
    classColumn = np.array(contactLensDS[:, numColumns - 1])
    # create a NB object
    nb = GaussianNB()
    # fit our data to the NB objects
    nb.fit(attColumns, classColumn)
    
    # predict any new test points
    testPoints = ([[0, 0, 0, 1]])
    predictions = nb.predict(testPoints)
    print(predictions)
    
    
    # use m - 4 (20) rows for training and the remaining 4 for testing.
    # creating the attribute columns array
    trainingSet = np.array(contactLensDS[0:numRows - 4, 1:numColumns - 1])
    # creating the classes column array
    trainingSetClasses = np.array(contactLensDS[0:numRows - 4, numColumns - 1])
    
    # fit our training set to our model
    nb.fit(trainingSet, trainingSetClasses)
    
    # creating our validation set
    # get rows starting at 4 rows before the end our our data and go through the end.
    validationSet = np.array(contactLensDS[numRows - 4:, 1:numColumns - 1])
    # get the class column for our validation set.
    validationSetClasses = np.array(contactLensDS[numRows - 4:, numColumns - 1])
    
    # predict using our validation set
    predictions = nb.predict(validationSet)
    print("predictions:", predictions)
    # check our predictions against the correct answers.
    print("correct answers:", validationSetClasses)
    
    for i in range(len(predictions)):
        print(i, ":", validationSetClasses[i], predictions[i])
        
    # writing it out to a text file.
    
main()