import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\geoportal.gdb"
env.overwriteOutput = True

fcList = arcpy.ListFeatureClasses()

for item in fcList:
    itemSRname = arcpy.Describe(item).SpatialReference.Name
    print itemSRname