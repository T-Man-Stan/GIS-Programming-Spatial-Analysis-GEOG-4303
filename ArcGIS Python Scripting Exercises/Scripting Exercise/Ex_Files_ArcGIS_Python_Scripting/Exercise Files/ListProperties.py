# ListProperties.py
# input paramenters: map document to process
# outputs: prints properties of a map document
# ArcMap 10.x
# October 18, 2018

# Import modules
import arcpy

# Create the map document object
mxd = arcpy.mapping.MapDocument(r"C:\Student\ICTPythonGIS\Maps\Belize.mxd")

# Print the properties
print "Existing title: ",mxd.title
mxd.title = "Map Showing Belize Mayan Sites, 2018"
print "New title: ",mxd.title
print mxd.author

mxd.save()
