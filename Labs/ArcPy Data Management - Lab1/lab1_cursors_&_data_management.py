# GIS 3
# Lab 1 student prototype

#import the modules needed
import arcpy
from arcpy import env

#set workspace

env.workspace = r'D:\lab1\data'
env.overwriteOutput = 1

soil = 'soil_sample.shp'

#create your list of year values
years = ["1972", "1973" , "1974" ,"1975","1976","1977","1978"]
print 'Creating iterable of years'


#buffer soil sample feature class
#for i in range(len(years)):

arcpy.Buffer_analysis(soil, 'soil_sample_Buf_500M.shp' , "500 Meters")

print 'Buffering soil layer'

#create search cursor for soil_sample.shp

for c in range(len(years)):
    arcpy.AddField_management('forestArea_'+years[c] + ".shp", "data_year","LONG")
    print 'added data_year to ' 'forestArea_'+years[c] + ".shp"
    arcpy.CalculateField_management('forestArea_'+years[c] + ".shp", "data_year",long(years[c]))
    print 'calculated field for data_year in ' 'forestArea_'+years[c] + ".shp"
    arcpy.Clip_analysis('forestArea_'+years[c]+".shp", 'soil_sample_Buf_500M.shp', 'forestArea_'+years[c]+'Buf_Soil_Clip.shp')
    print 'did clip for buffer and ' 'forestArea_'+years[c] + ".shp" " to make " 'forestArea_'+years[c]+".shp", 'soil_sample_Buf_500M.shp'
    arcpy.AddField_management('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "for_area","LONG")
    print 'added for_area to ' 'forestArea_'+years[c]+'Buf_Soil_Clip.shp'
    cursor=arcpy.da.SearchCursor('forestArea_'+years[c]+'Buf_Soil_Clip.shp',"SHAPE@AREA").next()
    area=cursor[0]
    arcpy.CalculateField_management('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "for_area",float(area))
    print 'calculated field for for_area in ' 'forestArea_'+years[c]+'Buf_Soil_Clip.shp'
    
    #part 2
    print "*****************************************"
    if arcpy.ListFields ('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "soil_smp"):
        arcpy.DeleteField_management ('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "soil_smp")
        arcpy.AddField_management('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "soil_smp","float")
    arcpy.AddField_management('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "soil_smp","float")
    cursor2=arcpy.da.SearchCursor('soil_sample.shp', 'year'+years[c]).next()
    soil_cursor=cursor2[0]
    arcpy.CalculateField_management('forestArea_'+years[c]+'Buf_Soil_Clip.shp', "soil_smp",float(soil_cursor))
    print 'calculated field for soil_smp '+ str(soil_cursor) + ' in ' 'forestArea_'+years[c]+'Buf_Soil_Clip.shp'
    print "The forest area in ",years[c], " was ",area," and the soil \
    measurement was ",soil_cursor
    
    print "-------------------------------------------------------------"

