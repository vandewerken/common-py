from glob import glob
import pyexcel as p 

### Set the following variables for the directory of the files you're working with

convertDirectory = 

### 

for convertOldXls in glob(convertDirectory + '*.xls'):

    xlsMinusPath = convertOldXls[:-3]
    xlsFileNewExtension = xlsMinusPath + "xlsx"

    p.save_book_as(file_name=convertOldXls, 
        dest_file_name=(newFileWithExtension))
    
    print("The workbook processed was: %s" % xlsFileNewExtension)

print("\n###\n" +
    "### The .xls TO .xlsx conversion was a success.\n" +
    "###\n")