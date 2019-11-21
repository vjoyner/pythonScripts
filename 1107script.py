#11/07/2019 Valarie Harrison
#Lecture

#us_major_cities average

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Harrison\ArcpyLesson1\UScitiesAvg.gdb\us_major_cities"
env.overwriteOutput = True

fc = "us_major_cities.shp"
fieldName0 = "NAME"
fieldName1 = "POPULATION"
print "worked"

rows = arcpy.da.SearchCursor(fc) #rows now cursor object
row = rows.next() #next method called from cursor object which returned row object

#while loop
while row:
    print str(row.getValue(fieldName0)) + "'s population is " + str(row.getValue(fieldName1)) + "."
    row = rows.next()
    
#for loop
for row in rows:
    print str(row.getValue(fieldName0)) + "'s population is " + str(row.getValue(fieldName1)) + "."

#da used to calculate average population
fc = "us_major_cities.shp"
count = 0
totalPop = 0

with arcpy.da.SearchCursor(fc, ("NAME","POPULATION")) as cursor:
    for row in cursor:
        totalPop += row[1]
        count += 1.0 #changes value of average to float
        
average = totalPop/count
print "average population is " + str(average)

#How to change value in row
fc = "us_major_cities.shp"
where = "CAPITAL" == 'State'
print where
with arcpy.da.UpdateCursor(fc, ("CAPITAL",)) as cursor:
    for row in cursor:
        print 