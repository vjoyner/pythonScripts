#11/14/2019 Valarie Harrison
#Lecture
#HW8 Review / Batch ReProjection

##import arcpy
##fc = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\geoportal.gdb\Fire"
##targetPrj = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\TNoutline_projected.shp"
##arcpy.Project_management(fc, r"H:\PythonGIS\Harrison\ArcpyLesson1\data\geoportal.gdb\Fire_reprojected", targetPrj)



import arcpy
##arcpy.env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\geoportal.gdb"
##fcList = arcpy.ListFeatureClasses("H*")
##print fcList

targetFc = r"H:\PythonGIS\Harrison\ArcpyLesson1\data1\data1\USA.gdb\TNoutline"
targetSR = arcpy.Describe(targetFc).Spatialreference.Name
##print targetSR
##outFolder = r"H:\PythonGIS\Harrison\ArcpyLesson1\data\USA.gdb\\"
##
##for fc in fcList:
##    fcSR = arcpy.Describe(fc).SpatialReference.Name
##    if fcSR != targetSR:
##        arcpy.Project_management(fc, outFolder+fc+"_projected", targetPrj)
##    else:
##        print "SR is same as target SR."

import arcpy
inFolder = arcpy.GetParameterAsText(0)
arcpy.env.workspace = inFolder
fcList = arcpy.ListFeatureClasses("T*")
print fcList

for fc in fcList:
    fcSR = arcpy.Describe(fc).SpatialReference.Name
    in fcSR != targetSR:
        arcpy.Project_management(fc, outFolder + fc[:-4] + "_projected.shp", targetSR)
    else:
        print "SR is same"
        
for fc in fcList:
    print fc