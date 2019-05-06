# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:35:35 2019
Trevor Stanley 
Lab5
Start - 3.12.19
Due - 4.2.19
@author: trst9490
"""
#see numpyIntro file lines 50-53 and 82-86 "numpy if and or conditionals"
#lab5 demo lines 48-56ish for ways to save data

# import modules
#******************************************************************************
from time import clock
start = clock()
print "Import Modules"
import arcpy
from arcpy import env
import arcpy.sa as sa
import numpy as np

#Set workspace environment
print 'Setting Workspace'
env.workspace = r"D:\lab5\data"
env.overwriteOutput = 1
arcpy.CheckOutExtension('Spatial')

#******************************************************************************

print "Define input DEM & NLCD:"
dem = 'dem_lab5' 
#landCover changed to lndCvr
lndCvr = 'nlcd06_lab5'

#NLCD Codes for reference:
# 11 - open water
# 12 perennial Ice/Snow
# Green area: 41, 42, 43, 51, 52
# Ag Land: 81 & 82
# Low Intensity Developed: 22 or 22
#slope of less than 8 degrees

#Part 1!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define Function
#******************************************************************************
print"Defining Functions"

def focalM(nparr):

    pGrid = np.zeros(nparr.shape).astype(float)
    for i in range (4,np.size(nparr,1)-5):
        for j in range (5,np.size(nparr,0)-6):
            sum = 0.0
            # now we will loop through our moving-window
            for ii in range(i-4,i+5):
                for jj in range(j-5,j+6):
                    sum = sum + nparr[jj,ii]
            pGrid[j][i] = float(sum/99.0)*100.0 
    return pGrid
    #print pGrid
    
  

def getCellSize(dem):
    description = arcpy.Describe(dem)  
    cellsize = description.children[0].meanCellWidth
    return cellsize

def getSlope(dem):
    outslope = Slope('demlab4', "DEGREE")
    outslope2 = outslope*(math.pi/180)
    return outslope2

# create raster objects
#******************************************************************************
print "Now Create Raster Objs:"
demRas = sa.Raster(dem)
coverRas = sa.Raster(lndCvr)

#Get raster information
demHeight = demRas.height
demWidth = demRas.height
nlcdHeight = coverRas.height
nlcdWidth = coverRas.height
llpnt = demRas.extent.lowerLeft
demSize = demRas.meanCellHeight
nlcdSize = demRas.meanCellHeight

assert(abs(demRas.meanCellHeight-demRas.meanCellWidth)<0.00001),'Cell size \.astype(float)significantly different'
assert(abs(coverRas.meanCellHeight-coverRas.meanCellWidth)<0.00001)

#convert raster objects to numpy arrays
demArr = arcpy.RasterToNumPyArray(demRas)
nlcdArr = arcpy.RasterToNumPyArray(coverRas)

#Get suitability indexes for each land cover criteria.
print "Now running the analysis for the green area"

#create a boolean array using where clause; then pass to the focal mean function 
nlcdGreen = np.where((nlcdArr == 41)|(nlcdArr==42)|(nlcdArr==43)|(nlcdArr==51)|(nlcdArr==52),1,0)
greenPer = focalM(nlcdGreen)
#print focalM(nlcdGreen)
greenSuit = np.zeros(nlcdGreen.shape).astype(float)
#checking if the percent green is larger than 30%; creates boolean grid of 1 & 0s based on this threshold
greenSuit = np.where((greenPer > 30.0),1,0).astype(float)

print "Now running the analysis for the agricultural area"
nlcdAgr = np.where((nlcdArr == 81)|(nlcdArr==82),1,0)
agrPer = focalM(nlcdAgr)
#print focalM(nlcdAgr)
agrSuit = np.zeros(nlcdAgr.shape).astype(float)
agrSuit = np.where((agrPer < 5.0),1,0).astype(float)  

print "Now running the analysis for the water area"
nlcdWet = np.where((nlcdArr == 11),1,0)
wetPer = focalM(nlcdWet)
wetSuit = np.zeros(nlcdWet.shape).astype(float)
wetSuit = np.where((wetPer > 5.0)&(wetPer < 20.0),1,0).astype(float) 

print "Now running the analysis for the low development area"
nlcdDev = np.where((nlcdArr == 21)|(nlcdArr==22),1,0)
devPer = focalM(nlcdDev)
devSuit = np.where((devPer < 20.0),1,0).astype(float)     

print "Now running the analysis for the slope"
demSlope = sa.Slope(demRas)
slopeArr = arcpy.RasterToNumPyArray(demSlope).astype(float)
slopePer = focalM(slopeArr)/100
slopeSuit = np.where((slopePer < 8.0),1,0).astype(float)

print "Now determining the suitability-index"
allSuit = np.zeros(nlcdArr.shape).astype(float)
allSuit = greenSuit + agrSuit + wetSuit + devSuit + slopeSuit

print "Sum up ALL the suitable sites!"
count = 0
for i in range (np.size(allSuit,1)):
    for j in range (np.size(allSuit,0)):
        if allSuit[j][i] == 5.0:
            count = count + 1
print "Number of suitable locations:",count

print "convert Numpy-array to arcpy-raster"
suitRaster = arcpy.NumPyArrayToRaster(allSuit,llpnt,demSize,demSize)
arcpy.DefineProjection_management(suitRaster,demRas.spatialReference)
print "Saving the Suitability Raster"
suitRaster.save('suitOut')
print 'elapsed time: ',round(clock()-start,2),' seconds'



#Circular Window 15*15
radius = (((.5+winRows)/2)**2(+((0.5+winCol)/2)**2)**0)

circdem = np.where((demArr < radius ),1,0)
#Vectorize operations
#Create Boolean Mask
if winShape =='rectangular':
    dim = int(dimList[0]/2),int(dimList[1]/2)]
    mask = np.ones((dim[0]))
