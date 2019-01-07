# ###############################################################
# Name:     ListDataFrames.py
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


# Loop through the data frames and print the data frame name


# Delete the variables
del strMapDocName,mxd,lstOfDataFrames
