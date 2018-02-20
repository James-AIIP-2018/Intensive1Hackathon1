'''
Created on 20 Feb 2018

@author: james + susan + seloke
'''
import math
import csv

# List initialisation
distanceSensors = []
    
# Open a csv file containing distance data
with open("at_distance_sensors.csv", "rU") as dataFile:
    
    rowCount=0
    # Read the dataset into a list
    csv_reader = csv.reader(dataFile, delimiter=',')
    for row in csv_reader:
        if rowCount <> 0:
            if row[0] == '':
                row[0] = 'end'
            if row[2] == '':
                row[2] = 0
            temp = [str(row[0]), float(row[1]), float(row[2])]
        rowCount = rowCount +1
