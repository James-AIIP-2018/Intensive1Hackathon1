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
            distanceSensors.append(temp)
        rowCount = rowCount +1
        


totalDistance = 1011.7959
cumulativeDistance = 0
for items in distanceSensors:
    if(items[0]<>'end'):
        cumulativeDistance = cumulativeDistance + items[1]
        temp = round(cumulativeDistance + items[2],4)
        if (temp <> totalDistance):
            print("Sensor: "+items[0]+", distance verification failed.")
   
    


# List initialisation
powerSupplySensors = []
powerSupplySensors_Filtered = []
    
# Open a csv file containing power supply data
with open("at_power_sensors.csv", "rU") as dataFile:
   
    rowCount=0
    # Read the dataset into a list
    csv_reader = csv.reader(dataFile, delimiter=',')
    for row in csv_reader:
        if rowCount <> 0:
            temp = [str(row[0]), float(row[1])]
            powerSupplySensors.append(temp)
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

for entry in powerSupplySensors:
    if(entry[1] < 0.995):
        error = entry[1]-0.995
        logger.info("SENSOR ERROR: Sensor: "+entry[0]+", Current power supply error: "+str(error))      
        temp = [entry[0], 0.9975]
        powerSupplySensors_Filtered.append(temp)
    else:
        temp = [entry[0], entry[1]]
        powerSupplySensors_Filtered.append(temp)

        