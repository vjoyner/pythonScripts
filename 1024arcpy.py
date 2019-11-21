#10/24/2019 Valarie Harrison
#arcpy lesson

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb"
##env.overwriteOutput = True
##
##fc = "Grocer" #fc is item name, can be changed to anything
##desc = arcpy.Describe(fc)
##for item in desc.fields: #Fields are in list, must access with for loop
##    print item.name, item.type, item.length
##
###<try> and <except> are a paired statement, will find errors from ESRI
##try:
##    arcpy.Buffer_analysis(fc, "Grocer_out", "1000 Metar",)
##except:
##    print arcpy.GetMessages() #Insert 0,1,2 to only print diff severity of error
##    
###LOOPING IN GIS MODELS
##
##fcList = arcpy.ListFeatureClasses()
##print fcList
##
##fcList = arcpy.ListFeatureClasses(wild_card = "C*")
##print fcList
##
##fcList = arcpy.ListFeatureClasses("C*")
##print fcList
##
##fcList = arcpy.ListFeatureClasses(feature_type = "Point")
##print fcList
##try:
##    for item in fcList:
##        arcpy.Buffer_analysis(item, item + "_bufferOut", "1000 Meter")
##except:
##    print arcpy.GetMessages()
##print "success!!!"



import arcpy
arcpy.env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\data\geoportal.gdb"
