### This file enables the user to loop through lines of a file, extract a string from a line, and use it to search for matches within another file

import csv
from glob import glob
import os

### Set the following variables for the directory of the files you're working with

processDirectory = '' # Enter directory of file with trailing forward slash in quotes 
searchFile = processDirectory + '' # Enter filename in single quotes 
matchFile = processDirectory + '' # Enter filename in single quotes 

### 

os.system('cls' if os.name == 'nt' else 'clear')
searchCounter = 0

with open(searchFile, 'r') as csvInMem:
    readingCSV = csv.reader(csvInMem, delimiter=',')
    rowCount = sum(1 for row in readingCSV)
    print('The total count of rows is: %s\n' % rowCount)

with open(searchFile, 'r') as csvInMem:
    readingCSV = csv.reader(csvInMem, delimiter=',')

    for row in readingCSV:
        lookForValue = row[2] # Should you need to return more than one matching columns in a search, comment out the following line
        #lookForValue2 = row[]

        with open(matchFile, 'r') as matchFileInMem:
            readingMatch = csv.reader(matchFileInMem, delimiter=',')
            for row in readingMatch:
                if lookForValue == row[1]:
                    with open(processDirectory + 'search_results.txt', 'a+') as resultsFile:
                        resultsFile.write(lookForValue + '\n')  # Should you need to return more matching columns in a search (see comment in Line 27)
                                                                # Add the variable with a delimiter before the new-line character here

        searchCounter += 1

        if searchCounter % 5 == 0:  # Set the denominator in the modulo to a realistic value for your data
                                    # e.g. if your record set is 100,000 rows, set to '10000' to get an update every 10,000 iterations
            print('The search is presently at record: %s\n' % searchCounter)
