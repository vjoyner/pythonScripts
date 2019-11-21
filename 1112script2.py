#11/12/19 part 2 Valarie Harrison

#Create Feature Class
#Arcpy3 PDF

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\geoportal.gdb"
##overwriteOutput = True
##
##arcpy.CreateFeatureclass_management(env.workspace, "insertPoint1", "Point", template = "Fire", spatial_reference = "Fire")

#Insert Cursor
inX = 790000
inY = 325367
fc = "insertPoint1"
inPoint = arcpy.Point(inX, inY)
rowInserter = arcpy.InsertCursor(fc)
newIncident = rowInserter.newRow()
colname = "FACILITY_ZIP"

newIncident.SHAPE = inPoint
newIncident.setValue(colname, "value")

rowInserter.insertRow(newIncident)
del rowInserter