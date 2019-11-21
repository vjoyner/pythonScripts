#10/29/2019 Valarie Harrison
#ArcPy Lecture

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb"

fc = "Grocer"
desc = arcpy.Describe(fc)
for item in desc.fields:
    print item.name, item.type, item.length

fc = "Grocer"
fieldList = arcpy.ListFields(fc)
for item in fieldList:
    print item.name