import arcpy

#print 'The first argument you entered is',sys.argv[1]
#print 'The second argument you entered is',sys.argv[2]
#print 'The name of the scxript is',sys.argv[0]


print 'The first argument you entered is',arcpy.GetParameter(0)
print 'The second argument you entered is',arcpy.GetParameter(1)
