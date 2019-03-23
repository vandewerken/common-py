import os
import csv
from xlsxwriter.workbook import Workbook
from glob import glob

### Set the following variables for the directory of the files you're working with

convertDirectory = 

### 

for csvfile in glob(convertDirectory + '*.csv'):
    csvFilename = os.path.basename(csvfile).split('.')[-2]
    workbook = Workbook(convertDirectory + csvFilename + '.xlsx', {'strings_to_numbers': True, 'constant_memory': True})            
    worksheet = workbook.add_worksheet()
    print csvfile

    with open(csvfile, 'rU') as f:
        r = csv.reader(f)
        for row_index, row in enumerate(r):
            for col_index, data in enumerate(row):
                worksheet.write(row_index, col_index, data)
    workbook.close()

    print("\n###\n" +
        "### The .csv TO .xlsx conversion was a success.\n" +
        "###\n")