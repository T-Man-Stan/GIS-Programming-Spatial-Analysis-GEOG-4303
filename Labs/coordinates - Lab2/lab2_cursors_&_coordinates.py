'''*********************************************
Author: Trevor Stanley
Date: 2/12/19
Purpose: Student prototype for lab 2
*********************************************'''

print "Importing variables"
# import necessary modules for the analysis
import sys, arcpy,traceback
from arcpy import env

env.workspace = "D:/lab2/data"

theme = 'colo14ers3.shp'


print "Declaring variables."
#Declare variables, i.e. existing and new ones you will need

CPrs = "route_coords.txt"
print "file exists"


print "*******Part I*********"
print "Reading the textfile."
#Read in the text file information line by line
#text = open(env.workspace + '/' + CPrs, 'r')
#use .strip() to remove the newline character (\n)
#note, when converting a numeric string to a float or int, \n stripped automatically

print "Creating the lists of x-y coordinate pairs."
CoordList = []
CoordListX = []
CoordListY = []
i=0
point = arcpy.Point()

with open(env.workspace + '/' + CPrs, 'r') as ins:
    CoordString = []
    for line in ins:
        #CoordString.append(line)
        CoordList.append([])
        CoordList[i] = [float(n) for n in line.split(',')]
        i = i+1
        
ins.close()

for i in range(len(CoordList)):
    CoordListX.append(CoordList[i][0])
    CoordListY.append(CoordList[i][1])

coords = zip(CoordListX,CoordListY)

features = arcpy.Array()

print "Creating a point object and an array object."

for i in range(len(CoordList)):
    print 'adding points to the new shapefile'
    point.X = coords[i][0]
    point.Y = coords[i][1]
    features.add(point)
    
print "Populating the line array with the point object"

poly = arcpy.Polyline(features)
arcpy.CreateFeatureclass_management(env.workspace, theme, "POLYLINE")
arcpy.AddField_management(theme, "numPnts", "FLOAT")
    
print "Opening an insert-cursor to create and access a new row." 

buildCur = arcpy.da.InsertCursor(theme,'SHAPE@')

print "Populating geometry with array"

buildCur.insertRow([poly])
arcpy.CalculateField_management(theme, 'numPnts', len(CoordList))
del buildCur

print "************** part II ****************"

print "Conducting 3D analysis"
arcpy.CheckOutExtension("3D") #Check out the extention 3D

print "Creating 3D shape"

feature3d = arcpy.InterpolateShape_3d(env.workspace + "/dem_lab2", theme, "colo14ers_interp5.shp")
interp = "colo14ers_interp5.shp"
fields = ["length2D", "length3D"]

dataset = env.workspace + "/dem_lab2"
spatial_ref = arcpy.Describe(dataset).spatialReference

print "Adding fields."
arcpy.AddField_management(interp, "length2D", "FLOAT")
arcpy.AddField_management(interp, "length3D", "FLOAT")

print "updating fields"
#use cursor to populate numPnts, 2D and 3D length fields
updCur3 = arcpy.UpdateCursor(interp)
updRow3 = updCur3.next()
updCur2 = arcpy.UpdateCursor(theme)
updRow2 = updCur2.next()

# get 2d length
len2d = updRow2.shape.length
updRow3.setValue('Length2D',len2d)
  
#get 3d Length
len3d = updRow3.shape.length3D
updRow3.setValue('Length3D',len3d)
    
#Update the attribute table row
updCur3.updateRow(updRow3)

del updCur2, updCur3,updRow2, updRow3 

print "finding lowest and highest Z values"

Z_cursor = arcpy.da.SearchCursor("colo14ers_interp5.shp", 'SHAPE@').next()

#initialize minimum and maximum values
min_X =0
min_Y=0
min_Z=99999999999999
max_X=0
max_Y=0
max_Z=0

#get min and max Z and assign X and Y values for these points
for row in Z_cursor:
    for points in row:
        for point in points:
            if point.Z < min_Z:
                print point.Z,"replacing",min_Z
                min_Z = point.Z
                print point.X,"replacing",min_X
                min_X = point.X
                print point.Y,"replacing",min_Y
                min_Y = point.Y
            if point.Z > max_Z:
                print point.Z, "replacing", max_Z
                max_Z = point.Z
                print point.X, "replacing", max_X
                max_X = point.X
                print point.Y, "replacing", max_Y
                max_Y = point.Y
del Z_cursor
     
print "The 2D length is:"
print len2d
print "The 3D length is:"
print len3d
print "The difference is:"
print len3d - len2d