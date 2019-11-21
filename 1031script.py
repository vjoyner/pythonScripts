#10/31/2019 Valarie Harrison
#Exercise Review

#H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb
#foxlake (raster), rec/TNoutline/us_boundary/us_states (polygon), us_cities (point), us_roads (polyline)

#H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb
#Community_Garden/Farmer_Market/Fire/Grocer/Health_Centers/Hospital/Law_Enforcement/Library/School (Points)
#County/Parks/Polygon (Polygon)
#Rail (Polyline)

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb"
env.overwriteOutput = True
outDir = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\\"
arcpy.CreateFileGDB_management(outDir, "newGDB.gdb")
outDir1 = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\newGDB.gdb\\"

fcList = arcpy.ListFeatureClasses(feature_type = "Point")
print fcList
for item in fcList:
    arcpy.Clip_analysis(item, "Polygon", outDir1 + item + "_clip")
    print item

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb"
env.overwriteOutput = True
print arcpy.ListRasters()

from arcpy.sa import *
inRaster = "foxlake"
cutoff = 3000
arcpy.CheckOutExtension("Spatial")
outRaster = Raster(inRaster) > cutoff
outRaster.save("fox3000")
 #re-evaluate to expand mask coverage
cutoff = 3500
arcpy.CheckOutExtension("Spatial")
outRaster = Raster(inRaster) > cutoff
outRaster.save("fox3500")
