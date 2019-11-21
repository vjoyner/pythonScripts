##11/19/2019 Lecture Script
##Valarie Harrison
import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb"
fc = r"H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb\us_states"
arcpy.MakeFeatureLayer_management(fc, "all")
where = """"STATE_ABBR" = 'TN'"""
print where
arcpy.MakeFeatureLayer_management(fc, "tn", where_clause = where)
arcpy.SelectLayerByLocation_management("all", "BOUNDARY_TOUCHES", "tn")
with arcpy.da.SearchCursor("all", "STATE_ABBR") as cursor:
    for row in cursor:
        print row[0]

#OPEN, Notepad exercise
gpsTrack = open(r"H:\PythonGIS\Harrison\gps_track.txt", "r")
print type(gpsTrack)
headerLine = gpsTrack.readline()
print headerLine
valueList = headerLine.split(",")
print valueList
print type(valueList)
latIndex = valueList.index("lat")
lonIndex = valueList.index("long")
print latIndex, lonIndex
coord = []
for line in gpsTrack.readlines():
    segLine = line.split(",")
    coord.append([segLine[latIndex], segLine[lonIndex]])
print coord
