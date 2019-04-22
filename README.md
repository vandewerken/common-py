# Common-py

This repo offers a collection of routines that can be incorporated into other python functions and scripts or used individually. I regularly find myself recreating this functionality, so I've decided to create a common reference here. 

These routines include functionality for file manipulations, parsing, and search. I've already been through the StackOverflow rabbitholes, and these are what I've found to be the most optimal solutions to each of the issues presented. 

I'm releasing under an MIT license, so feel free to clone / modify as necessary. 

___

This repo contains scripts for the following: 

* `search_within.py` loops through the rows of one csv file for strings and searches within a second csv file for matches
* `convert_csv_xlsx.py` converts csv files to xlsx files for a specified directory
* `convert_txt_xlsx.py` converts txt files to xlsx files for a specified directory
* `convert_xls_xlsx.py` converts xls files to xlsx files for a specified directory
* `copy_range_xlsx.py` copies a range or ranges from one xlsx workbook to another
* `combine_single_ws.py` consolidates entire worksheets from separate workbooks into the same sheet in the same workbook. 