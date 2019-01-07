# #################################################################
# Name:     ReadWritLoop.py
# Purpose:  To demonstrated how to write multiple records to a file
# Inputs:   A map document
# Outputs:  output text file
# Author:   J. Harrison
# Date:     10/18/2018
# #################################################################

# import modules
import arcpy

# create the map document object
strMapDoc = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Maps\Fields.mxd'

                                
# open the output file
# path should be updated to match local directories
strOutFile = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Data\BrokenLinks.txt'


# print the header records to the output file


# create the list of broken links


# loop through the list of broken layers, printing the laye rname


# close the output file
outFile.close()

# delete the variables
del strOutFile,mxd,strMapDoc,
