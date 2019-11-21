#11/12/19 Valarie Harrison


###Search Cursor
##import arcpy
##fc = r"H:\PythonGIS\Harrison\us_major_cities\us_major_cities.shp"
##where = '"POPULATION" > 950000'
##where1 = """"NAME" Like 'S%'"""
##where2 = """"CAPITAL" = 'State capi'"""
##
#####with arcpy.da.SearchCursor(fc,("NAME","POPULATION", "SHAPE@XY"),where_clause = where1) as cursor: #Option, create tuple
####with arcpy.da.SearchCursor(fc,["NAME","POPULATION", "SHAPE@XY"],where_clause = where1) as cursor:  #Option, create list
####    for row in cursor:
####        print row[0], row[1], row[2]
##
###UpdateCursor updates a row object to new value
##with arcpy.da.UpdateCursor(fc,"CAPITAL", where) as cursor:
##    for row in cursor:
##        row[0] = "State"
##        cursor.updateRow(row)

#InsertCursor
