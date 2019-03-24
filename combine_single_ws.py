import os
import getpass
import pandas as pd
from glob import glob


### Set the following variables for the directory of the files you're working with

processDirectory = 
createNewWorkbookPath = 

### 

excelFiles = glob(processDirectory + '*.xlsx')
excels = [pd.ExcelFile(name) for name in excelFiles]
frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]
frames[1:] = [df[1:] for df in frames[1:]]
combined = pd.concat(frames)
combined.to_excel(createNewWorkbookPath, header=False, index=False)

print("\n\n###\n" +
    "### The combine script was a success\n" + 
    "###")

