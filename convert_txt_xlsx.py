import openpyxl    
import os              

### Set the following variables for the directory of the files you're working with

convertDirectory = 

### 

for txtfile in glob(convertDirectory + '*.txt'):
    txtFilename = os.path.basename(txtfile).split('.')[-2]
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]

    with open(txtfile, 'rb') as f:
        reader = csv.reader(f, delimiter='') # this routine presumes that values are split using a delimiter which must be specified here
        for row in reader:
            ws.append(row)
    print txtfile

    wb.save(convertDirectory + txtFilename + '.xlsx')
    wb.close()

    print("\n###\n" +
        "### The .txt TO .xlsx conversion was a success.\n" +
        "###\n")