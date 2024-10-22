# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:25:33 2024
Shell for HW 5
@author: DC Cline
"""

import pandas as pd
import math


def main():
    # Read in the CSV and transpose it
    # Don't worry about the dataframes for now, we're just using it as an 
    # intermediate way to create a dictionary
    df = pd.read_csv("Weather05.csv")   
    df = df.transpose()
    dictionary = df.to_dict()  
    
    printTable(dictionary)
    
    # Call the countOccurrences method
    print("Number of 'overcast': ", countOccurrences(dictionary, "overcast"))
    print("Number of 'False': ", countOccurrences(dictionary, False))
    
    # Create a dictionary of the number of times particular words occur
    # in a column and print it out
    groupsDictionary = countGroupsInAttribute(dictionary, "outlook")
    print("Counts for attribute 'outlook'")
    for groups in groupsDictionary.keys():
        print(groups, groupsDictionary[groups])
        
    groupsDictionary = countGroupsInAttribute(dictionary, "play")
    print("Counts for attribute 'play'")
    for groups in groupsDictionary.keys():
        print(groups, groupsDictionary[groups])
    
    # Find the closest "weather" row to each of these rows
    print("Closest to 0: ", findClosest(dictionary, 0))
    print("Closest to 5: ", findClosest(dictionary, 5))
    
    
# Print out as a table

def printTable(dictionary):
    # This prints out the headers including an ID column
    print("ID", end="\t")
    for name in dictionary[0].keys():
        print(name, end="\t\t")
    print()
    # Tkey automatically assigned is 1 through 13
    for key in dictionary:
        print(key, end="\t\t")
        # Retrieve that particular row
        row = dictionary[key]
        # For each attribute in that row, print out value of that row
        # for that attribute
        for value in dictionary[key]:
            print(row[value], end="\t\t")
        print()
    print()
    
# This method takes in a rowID (0 through 13) and calculates its weather
# See the assignment description for the meaning of weather
# The it find the row (besides itself) that has the most similar weather
# That is: The absolute value of the difference is the smallest
def findClosest(dictionary, rowID):
    # find the weather value for the chosen row
    chosenRow = dictionary[rowID]
    chosenWeather = chosenRow['temperature'] + chosenRow['humidity']
    # initialize chose weather
    closestWeather = chosenWeather
    # iterate through the rows
    for i in dictionary:
        # find the current row's weather value
        currentRow = dictionary[i]
        currentWeather = currentRow['temperature'] + currentRow['humidity']
        # if closer and not chosen row, set closest to this row.
        if abs(chosenWeather - currentWeather) < closestWeather and i != rowID:
            closest = i
            closestWeather = abs(chosenWeather - currentWeather)
    return closest
            
# This method searches for the specified value in the whole table 
# That is: (all rows/all columns)
def countOccurrences(dictionary, value):
    number = 0
    for i in dictionary:
        # retrieve row
        row = dictionary[i]
        # iterate through the row
        for j in row:
            # if the value is in the row, add an occurance
            if row[j] == value:
                number += 1
    return number

# This creates a dictionary based on the attribute column passed in
# The key for each entry coresponds to the unique values 
# (for example, sunny/overcast, etc for outlook)
# The value is the number of times it shows up (so at least 1)
# Use the "if - in" function to see if an item is already in the dictionary

def countGroupsInAttribute(dictionary, attribute):
    attributes = dict()
    # iterate through the dictionary
    for i in dictionary:
        row = dictionary[i]
        # if the attribute is in the attributes dict,
        # add one to the count of this attribute
        if row[attribute] in attributes:
            attributes[row[attribute]] += 1
        else:
        # if not in the dict, add the attribute to the dict.
            attributes[row[attribute]] = 1
            
            
    return attributes
    
main()