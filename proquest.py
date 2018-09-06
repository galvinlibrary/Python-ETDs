import sys
import os, os.path
import numpy

home = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\unzipped'

## get list of subdirectories
subs_list = []
for wd, subs, files in os.walk(home):
    subs_list.append(wd)
    
del subs_list[0]
#print(subs_list[0])

# Find largest file, save name as a variable    
def findbig(home):
    def sortSecond(val):
        return val[1]
    
    contents = os.listdir(home)
    size_array = []
    
    for i in contents:
        size = (i, os.path.getsize(home + "\\" + i ) )
        size_array.append(size)
        
        
    size_array.sort(key=sortSecond, reverse=True)
    bigfile = size_array[0][0]
    shortname = bigfile.split(".")[0]
    # Check if extra metadata file exists, rename xml file to run against xslt 
    if shortname + "_DATA.xml" in contents:
        os.rename(home + "\\" + shortname + "_DATA.xml", home + "\\proquest.xml")
    else:
       pass
    print(bigfile, shortname)
    print(contents)
for d in subs_list:
    findbig(d)
