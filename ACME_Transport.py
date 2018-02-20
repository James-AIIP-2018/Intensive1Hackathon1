'''
Created on 20 Feb 2018

@author: james + susan + seloke
'''
import math
import csv

# Dataset list initialisation
distanceSensors = []
    
# Open a csv file containing distance data
with open("at_distance_sensors.csv", "rU") as dataFile:
    
    rowCount=0
    # Read the dataset into a list row by row
    csv_reader = csv.reader(dataFile, delimiter=',')
    for row in csv_reader:
        
        # Ignore the first row (headers)
        if rowCount <> 0:
            # If this is the last row 
            if row[0] == '':
                row[0] = 'end'
            if row[2] == '':
                row[2] = 0
                
            # Write a temporary list containing row data
            temp = [str(row[0]), float(row[1]), float(row[2])]
            
            # Append the list (row) to the dataset list
            distanceSensors.append(temp)
        
        # Increment the row counter
        rowCount = rowCount +1
        

# Define the total distance
totalDistance = 1011.7959

# Initialise the cumulative distance
cumulativeDistance = 0

# Loop through the distance dataset
for items in distanceSensors:
    if(items[0]<>'end'):
        
        # Update the cumulative value to include the new delta value
        cumulativeDistance = cumulativeDistance + items[1]
        
        # Calculate the expected total distance and round to 4 decimal places 
        expectTotalDistance = round(cumulativeDistance + items[2],4)
        
        
        if (expectTotalDistance <> totalDistance):
            print("Sensor: "+items[0]+", distance verification failed.")
   
    


# List initialisation
powerSupplySensors = []
powerSupplySensors_Filtered = []
    
# Open a csv file containing power supply data
with open("at_power_sensors.csv", "rU") as dataFile:
   
    rowCount=0
    # Read the dataset into a list row by row
    csv_reader = csv.reader(dataFile, delimiter=',')
    for row in csv_reader:
        # Ignore the first row (headers)
        if rowCount <> 0:
            # Write a temporary list containing row data
            temp = [str(row[0]), float(row[1])]
            # Append the list (row) to the dataset list
            powerSupplySensors.append(temp)
        # Increment the row counter
        rowCount = rowCount +1


# Setup logging 
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Logging filename: sensorErrors.log in write mode (will overwrite existing log file)
handler = logging.FileHandler('sensorErrors.log', 'w')

# Set logging format to include the date and time, logging level and the actual logging message
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

# Loop through power supply dataset
for entry in powerSupplySensors:
    # If the power supply falls below acceptable range
    if(entry[1] < 0.995):
        # Calculate the error (below range) and log
        error = entry[1]-0.995
        logger.info("SENSOR ERROR: Sensor: "+entry[0]+", Current power supply error: "+str(error))      
        # Filter below values to 0.9975 and add to filtered list
        temp = [entry[0], 0.9975]
        powerSupplySensors_Filtered.append(temp)
    else:
        # Append valid power supply to filtered list
        temp = [entry[0], entry[1]]
        powerSupplySensors_Filtered.append(temp)
        
    # Print Early warning
    if(entry[1] < 0.996):
        print("EARLY WARNING: Power Supply: "+str(entry[0]+" is below 0.996."))

        