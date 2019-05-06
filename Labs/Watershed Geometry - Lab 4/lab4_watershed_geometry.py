'''
author: Trevor Stanley
date: 3.12.19
Lab 4
'''

#import modules
print "Importing Modules"
import arcpy,os, math, numpy
from arcpy import env
from arcpy.sa import*
arcpy.CheckOutExtension("Spatial")
import stanley_lab4_module2
#Set workspace environment
print 'setting workspace'
#env.workspace = r"D:\lab4\data"

#set env properties
env.workspace = os.getcwd()+'\data'
env.overwriteOutput = 1

#******************************************************************************
# Part 1

# Calling Functions
#******************************************************************************



print "Declaring Variables"
labdem = "demlab4"
wtrshed = "watersheds_3D.shp"
dem = Raster('demlab4')
zonal_out = 'SA.dbf'

print "Call ALL THE FUNCTIONS!"
twoDP = stanley_lab4_module2.twoDP(wtrshed)
twoDA = stanley_lab4_module2.twoDA(wtrshed)
circR = stanley_lab4_module2.circR(wtrshed)
threeDP = stanley_lab4_module2.threeDP(wtrshed)
threeDA = stanley_lab4_module2.threeDA(wtrshed)
circR3D = stanley_lab4_module2.circR3D(wtrshed)
threeDPZmin = stanley_lab4_module2.threeDPZmin(wtrshed)
threeDPZmax = stanley_lab4_module2.threeDPZmax(wtrshed)
centroid = stanley_lab4_module2.centroid(wtrshed)
LCA = stanley_lab4_module2.LCA(wtrshed)
FarthestP = stanley_lab4_module2.FarthestP(wtrshed)




print "Writing fields to watershed shp file!"
print "*****************************************"

arcpy.AddField_management(wtrshed,'circ_2D',"FLOAT")
arcpy.AddField_management(wtrshed,'circ_3D',"FLOAT")
uCur = arcpy.UpdateCursor(wtrshed)
n_poly = int(arcpy.GetCount_management(wtrshed).getOutput(0))

print "Now we compare our 2D & 3D circularity ratios!"
print "**************************************************"

for i in range(n_poly):
    rows = uCur.next()
    rows.circ_2D = circR[i]
    rows.circ_3D = circR3D[i]
    uCur.updateRow(rows)
    print "2D circularity ratio for this polygon",i+1,"is",circR[i]
    print "3D circularity ratio for this polygon",i+1,"is",circR3D[i]
    print "**************************************************"
del uCur, rows

print "Fields Circ_Ra_2d and Circ_Ra_3d updated and compared"

#******************************************************************************
# Part 2

# calling the relief-ratio func!
#******************************************************************************


relief = stanley_lab4_module2.relief_Ratio(wtrshed)       
print "Add those ratios to the attribute table!"

arcpy.AddField_management(wtrshed,"Relief_Ra","FLOAT")
upCur = arcpy.UpdateCursor(wtrshed)
for i in range(n_poly):
    rows = upCur.next()
    rows.Relief_Ra= relief[i]
    upCur.updateRow(rows)
    print "2D circularity ratio for this polygon",i+1,"is",relief[i]
    
del upCur, rows
    
    
print twoDP
print "______________________"
print twoDA
print "______________________"
print circR
print "______________________"
print threeDP
print "______________________"
print threeDA
print "______________________"
print circR3D
print "______________________"
print threeDPZmin
print "______________________"
print threeDPZmax
print "______________________"
print centroid
print "______________________"
print LCA
print "______________________"
print FarthestP
print "______________________"