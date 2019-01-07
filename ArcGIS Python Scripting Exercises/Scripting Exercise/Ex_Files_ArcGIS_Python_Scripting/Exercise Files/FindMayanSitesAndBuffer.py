# FindMayanSitesAndBuffer.py
# input paramenters: Name of Mayan Site, buffer distance
# works on CURRENT map document
# outputs: New polygon feature class (the buffer)
# ArcMap 10.x
# October 18, 2018

# Import modules
import arcpy

# Create the map document object
mxd = arcpy.mapping.MapDocument("CURRENT")

# Get the inputs from the user
strName = arcpy.GetParameterAsText(0)
numBufDist = arcpy.GetParameterAsText(1)

# Select the site and buffer it
arcpy.SelectLayerByAttribute_management("MayanSites","New_Selection","ucase(BWNAME) = \'"+strName+"\'")
arcpy.Buffer_analysis("MayanSites","site_buff",numBufDist)
