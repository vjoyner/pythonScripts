# Gabriela Boaventura
# Oct 24, 2019
# Make up Class, working with arcpy environment workspace

#If you are using the script bellow, make sure to declare the syntax assign to this kind of module
##import arcpy

# Here the import sprit taking all the descriptive modules from arcpy to environment space
from arcpy import env

# important to get the corect path to facilite the location of data 
env.workspace = r"H:\PythonGIS\Boaventura\data\data"
fc = "geoportal.gdb/Fire"
# fc stands for feature class but could be any other given name

# another option 
#fc = r"H:\PythonGIS\Boaventura\data\data\geoportal.gdb"
# another optio is 
env.workspace = r"H:\PythonGIS\Boaventura\data\data\geoportal.gdb"
fc = "Fire" # here I have my object which is a string data type

# Have to assign a variable which now is describing an object. Return Value
desc = arcpy.Describe(fc)

print desc.shapeType
print desc.featureType
print desc.hasOID
print desc.fields

#fields returnd a list but need to be acess each item from the list
#DO THIS
for item in desc.fields:
    print item.name, item.length

print desc.extent.XMin


