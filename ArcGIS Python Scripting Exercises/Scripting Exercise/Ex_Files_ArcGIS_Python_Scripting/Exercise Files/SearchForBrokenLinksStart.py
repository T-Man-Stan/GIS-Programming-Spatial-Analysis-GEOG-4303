# #################################################################
# Name:     SearchForBrokenLinks.py
# Purpose:  Finds Broken Links in a File
# Inputs:   A map document
# Outputs:  output text file
# Author:   J. Harrison
# Date:     10/18/2018
# #################################################################

# import modules
import arcpy

# create the map document object
strMapDoc = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Maps\Fields.mxd'
mxd = arcpy.mapping.MapDocument(strMapDoc)
                                
# open the output file
# path should be updated to match local directories
strOutFile = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Data\BrokenLinks.txt'
outFile = open(strOutFile,'w')

# print the header records to the output file
print >> outFile, 'Broken Layers Report'
print >> outFile, mxd.title

# create the list of broken links
lstBroken = arcpy.mapping.ListBrokenDataSources(mxd)

# loop through the list of broken layers, printing the laye rname
for eachLyr in lstBroken:
    print >> outFile,eachLyr.name + '-' + eachLyr.dataSource

# close the output file
outFile.close()

# delete the variables
del strOutFile,mxd,strMapDoc,
