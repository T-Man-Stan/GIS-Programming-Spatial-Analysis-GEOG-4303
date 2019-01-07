# ###############################################################
# Name:     WorkWithLists.py
# Purpose:  To demonstrated how to use lists to get to layers
# Inputs:   A map document
# Outputs:  Layer names are printed to the screen
#           are printed to the screen
# Author:   J. Harrison
# Date:     10/18/2018
# ###############################################################

# Import modules
import arcpy

# Create the map document object
mxd = arcpy.mapping.MapDocument(r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Maps\Belize.mxd')

# Create the list of layers
lstOfLayers = arcpy.mapping.ListLayers(mxd)

# Loop through the list of layers
for eachLyr in lstOfLayers:
    print eachLyr.name

# Delete the variables
del mxd
