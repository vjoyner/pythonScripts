#10/22/2019 Valarie Harrison
#Arcpy lesson 1

#describe function

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb" #to keep \ in path name, must put r (raw) as \ is exit statment in pyton
desc = arcpy.Describe("School")
print "Shape type: " + desc.shapeType #shapeType same as geometry type, though cannot call as geometry type in python
print "hasM: " + str(desc.hasM) #desc.hasM must be forced into string, as data type is boolean and will create syntax error
print "Feature type: " + desc.featureType
print desc.shapeFieldName
print desc.spatialReference #returns value, but not specific value that we are looking for
print desc.spatialReference.name #without .name, it will return different value that gives memory location and not spacial ref name
print desc.extent #returns value, but not specific value that we are looking for, gives full extent in specific format
print desc.extent.XMin #for specific location of specific extent


