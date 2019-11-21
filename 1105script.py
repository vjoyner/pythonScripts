#11/05/2019 Valarie Harrison

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb"
##env.overwriteOutput = True
##
##fc = arcpy.GetParameterAsText(0)
##fc_out = arcpy.GetParameterAsText(1)
##distance = arcpy.GetParameterAsText(2)
##arcpy.Buffer_analysis(fc, fc_out, distance)
##
##arcpy.AddMessage(arcpy.GetMessages())
##print "Buffer Complete!"

#Object Cursor**********************
# types:
    #search cursor : accessing data row vertically, read only functionality
    #update cursor : replace values
    #insert cursor : create new data row, ex. insert new points in attribute table of fire layer, or polygon in parks layer
#Create search cursor arcpy.SearchCursor()
#Call SearchCursor.next() to read first row, start loop that will exit when there are no more rows
#Do something with values in current row
#Call SearchCursor.next() to move to next row, b/c loop was created, this puts you back at prev step if another row is available to read

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb"
env.overwriteOutput = True

fc = "us_cities"
print "worked"

rows = arcpy.SearchCursor(fc)
row = rows.next()

while row:
    print row.NAME
    row = rows.next()


    
    