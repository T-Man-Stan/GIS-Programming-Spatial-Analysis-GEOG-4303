# ###############################################################
# Name:     WorkWithMapDocs.py
# Purpose:  To demonstrated how to get to map document properties
# Inputs:   A map document
# Outputs:  Map document author, dates saved and active data frame
#           are printed to the screen
# Author:   J. Harrison
# Date:     10/18/2018
# ###############################################################

# Import modules
import arcpy

# Set a variable to hold the name of the map document that we want to check
strMapDoc = r'C:\Users\Jennifer Harrison\Desktop\Exercise Files\Maps\Belize.mxd'

# Instantiate the map document object (grab ahold of the map document)
mxd = arcpy.mapping.MapDocument(strMapDoc)

# Print a message to the user that you are checking the map document properties
print 'Checking the properties of:', strMapDoc

# Print the map document’s author name, the date saved and the name of the active data frame
print 'Map Author:', mxd.author
print 'Date Saved:',mxd.dateSaved
print 'Active Data Frame:', mxd.activeDataFrame.name


# Reset the map’s title
mxd.title = 'This is the map where I fixed the properties.'

# Save the map
mxd.save()

# Print a message to the user saying that the script has completed its task
print 'Completed checking the properties of',strMapDoc

# Delete the variables
del strMapDoc,mxd
