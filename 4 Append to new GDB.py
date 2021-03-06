# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Shapfile AddEditInfo & rename
# "for" loop
# ListDatasets.py
# Append.py
# Created on: 2021-05-13 17:53:09.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os

# main path
arcpy.env.workspace = "D:\\OSM\\united states of america for Append.gdb\\"

# Get all contents in GDB.
datasets1 = arcpy.ListDatasets(feature_type='feature')
datasets2 = [''] + datasets1 if datasets1 is not None else []

for ds in datasets2:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        railway_work = os.path.join(arcpy.env.workspace, ds, fc)    

        railway = "_railway"

        # Append railway to new GDB.
        if railway in railway_work:
            railway_target_path = "D:\\OSM result\\North America.gdb\\"
            railway_emptyFC = "United_States_railway"
            schemaType = "No_TEST"
            arcpy.Append_management(railway_work, railway_target_path + railway_emptyFC, schemaType, "", "")
            print (railway_work + " features are Append.")

        # Append road to new GDB.
        else:
            road_target_path = "D:\\OSM result\\North America.gdb\\"
            road_emptyFC = "United_States_road"
            schemaType = "No_TEST"
            arcpy.Append_management(railway_work, road_target_path + road_emptyFC, schemaType, "", "")
            print (railway_work + " features are Append.")    
    
print ("Finished.")