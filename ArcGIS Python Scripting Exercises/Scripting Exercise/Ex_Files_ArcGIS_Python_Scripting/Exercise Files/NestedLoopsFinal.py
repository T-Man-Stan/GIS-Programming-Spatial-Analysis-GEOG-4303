# ###############################################################
# Name:     NestedLoops.py
# Purpose:  To demonstrated how to use lists to get to data frames
# Inputs:   A map document
# Outputs:  All layer classes used in the map document are listed
# Author:   J. Harrison
# Date:     10/18/2018
# ###############################################################

# Import modules
import arcpy

# Create the map document object
strMapDocName = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Maps\Belize2.mxd'
mxd = arcpy.mapping.MapDocument(strMapDocName)

# Create the list of data frames
lstOfDataFrames = arcpy.mapping.ListDataFrames(mxd)

# Loop through the data frames and print the data frame name
numCount = 1
for eachDataFrame in lstOfDataFrames:
    print 'Checking Data frame',numCount,':\t',eachDataFrame.name
    numCount = numCount+1
        
#   Loop through the layers and print the layer name
    lstOfLayers = arcpy.mapping.ListLayers(mxd,'*',eachDataFrame)
    for eachLyr in lstOfLayers:
        print 'Layer name: ',eachLyr.name
        for eachLabelClass in eachLyr.labelClasses:
            print 'Label Name:\t',eachLabelClass.className
            print 'SQL Query:\t',eachLabelClass.SQLQuery
            print '-------------'
#       Loop through the lable classes and print some properties

# Delete the variables
del strMapDocName,mxd,lstOfDataFrames, lstOfLayers
