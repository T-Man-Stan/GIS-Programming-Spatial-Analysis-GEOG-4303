#Audio from GIS Lab 2.12.19 for some discussion on for loop part
"""
Lab 3 2.26.19
Created on Tue Feb 12 12:59:08 2019

@author: Trevor Stanley -- trst9490
"""
# import necessary modules for the analysis
print 'importing modules'
import arcpy
from arcpy import env
#Set workspace environment
print ' setting workspace'
env.workspace = r"D:\lab3\data"

env.overwriteOutput = 1
arcpy.CheckOutExtension('Spatial')


def pntMkr(point,row):
    # This function creates a point featureclass from 
    # the list of x coords & y coords. The params are a point
    # featureclass & a new row to place the point.
    
    point.X = XCoords[i]
    point.Y = YCoords[i]
    print 'point properties (from within our function): '
    print "X: ", point.X, "Y: ", point.Y
    row.shape = point
    print "---------------------------------"
    pointCur.insertRow(row)


#Create vars
print 'declaring ALL the variables'

#Var for interest area polygon
IA_shp = 'interestAreas.shp'
#Var to store grid points for every interest polygon
pointsList= ['grid1.shp','grid2.shp','grid3.shp']
#Var to store buf polygons for every gridpoint
pointsBuff = ['gridbuff1.shp','gridbuff2.shp','gridbuff3.shp']
#Create var to store square buf list
squareBuff = ['squarebuff1.shp','squarebuff2.shp','squarebuff3.shp']
#Var to store our clipped bufs- (ie our interest areas)
pointClip = ['gridclip1.shp','gridclip2.shp','gridclip3.shp']
squareClip = ['squareclip1.shp','squareclip2.shp','squareclip3.shp']

#Variable to store the 1992 agriculture raster.
AgrLand = ['agr1992','agr2001']

#stats changed to DBF_stats
DBF_stats = ['g1agr1992.dbf','g2agr1992.dbf','g3agr1992.dbf','g1agr2001.dbf','g2agr2001.dbf','g3agr2001.dbf']

#declare pntMkr function here
print "Declaring the pntMkr function"


print "*************** Part I ********************"

print "Creating our Poly Mesh, XCoord, and YCoord Lists"

#Create a list of mesh size
#list containing mesh sizes
polyList = [2000,3500, 4500]

#Empty lists created to store coords
XCoords = []
YCoords = []

#Create search cursor in the interestAreas.shp file
print "Creating Search Cursor"
SCur = arcpy.SearchCursor(IA_shp)
#could do arcpy.da.SearchCursor (will be faster)

print "--------------------Begin Looping------------------"

#Iterate three times in order to get the extents of every polygon
#perform computations within the nested loops
#range has a third parameter for distance to jump
#Look into multipoint feature on Arc online
#also look into arcpy array for easier input into featureclass
for i in range(len(polyList)):
    row = SCur.next()
    ext = row.shape.extent
    xM = ext.XMin
    xMa = ext.XMax
    yM = ext.YMin
    yMa = ext.YMax
    #Fill our lists XCoords & YCoords
    while yM < yMa:
        if xM < xMa:
            XCoords.append(xM)
            YCoords.append(yM)
            xM = xM + polyList[i]
        else:
            yM = yM + polyList[i]
            xM = ext.XMin
    #create new featureclass; file isnt specified tho?
    #will likely need to do + '/' + IA_shp
    arcpy.CreateFeatureclass_management(env.workspace, pointsList[i], "point")
    pointCur = arcpy.InsertCursor(pointsList[i])     
    print"Making Points!"
    point = arcpy.Point()
    row = pointCur.newRow()
    
    # Create a new feature class of points named "grid.shp"
    for i in range(0,len(XCoords)):
        print 'Executing pntMkr function!'
        #declared pntMkr above
        pntMkr(point,row)
        
    del pointCur
    XCoords = []
    YCoords = []   
del SCur, row


#The below code allows one to select a square or round buffer 
#Change the below code such that specific file name and indexes are altered to be own
usInpt = raw_input("enter R for Round buffer zones or S for square buffers zones: ")

for i in range(0,len(pointsList)):
    if usInpt == 'R':
        print "Now buffering each point by 500 meters"
        arcpy.Buffer_analysis(pointsList[i],pointsBuff[i],"500 meters")
        print "Now clipping sample zone (gridbuff.shp) to IA_shp"
        arcpy.Clip_analysis(pointsBuff[i],IA_shp,pointClip[i])
    elif usInpt == 'S':
        print "Now buffering each point by 500 meters"
        arcpy.Buffer_analysis(pointsList[i],pointsBuff[i],"500 meters")
        arcpy.FeatureEnvelopeToPolygon_management (pointsBuff[i], squareBuff[i], "MULTIPART")
        arcpy.Delete_management(pointsBuff[i])
        print "Now clipping sample zone (gridbuff.shp) to IA_shp"
        arcpy.Clip_analysis(squareBuff[i],IA_shp,squareClip[i])
        
print"Executing Zonal Statistics"

if usInpt == 'R':
    for i in range(0,len(AgrLand)):
        for j in range(0,len(pointClip)):
            for k in range(0,len(DBF_stats)):
                arcpy.sa.ZonalStatisticsAsTable(pointClip[j],'id',AgrLand[i],DBF_stats[k],'DATA','MEAN')
                sCur = arcpy.SearchCursor(DBF_stats[k])
                zrow = sCur.next()
                mean = zrow.getValue("MEAN")
            print 'The calculated avg intensity of ag land in',AgrLand[i],"for our interest area",pointClip[j],"is", mean
if usInpt == 'S':
    for i in range(0,len(AgrLand)):
        for j in range(0,len(squareClip)):
            for k in range(0,len(DBF_stats)):
                arcpy.sa.ZonalStatisticsAsTable(squareClip[j],'id',AgrLand[i],DBF_stats[k],1,'MEAN')
                sCur = arcpy.SearchCursor(DBF_stats[k])
                zrow = sCur.next()
                mean = zrow.getValue("MEAN")
            print 'The calculated avg intensity of ag land in',AgrLand[i],"for our interest area",squareClip[j],"is", mean
            
print "All done!!!"