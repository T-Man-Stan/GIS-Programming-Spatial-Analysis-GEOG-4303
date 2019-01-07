# ###############################################################
# Name:     WorkWithMReadWriteFile.py
# Purpose:  To demonstrated how to read from and write to a file
# Inputs:   input text file
# Outputs:  output text file
# Author:   J. Harrison
# Date:     10/18/2018
# ###############################################################

# import modules
import arcpy

# open the input and output files
# path should be updated to match local directories
inFile = open(r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Data\FileList.txt','r')
outFile = open(r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Data\UpdatedFileList.txt','w')

# read the first record


# print the record back out


# close the files
inFile.close()
outFile.close()

# delete the variables
del strRecord,strField1,strField2,strField3
