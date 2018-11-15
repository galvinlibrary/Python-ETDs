import os
import shutil
import csv


def move(src, dest):
    shutil.move(src, dest)

home = 'C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\masters'
zip_done = 'C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\masters_compound'

dir_counts = []
compounds = []

for dirs, subs, files in os.walk(home):
    contents = os.listdir(dirs)
    count = len(contents)
    #row = (dirs, count)
    #dir_counts.append(row)

    # Move compound object directories
    if count > 8:
        compounds.append(dirs)
    else:
        pass
    
    #print(row)
del compounds[0]
print(compounds)

for d in compounds:
    move(d, zip_done)

## Create log file with directory name and file counts
#print(dir_counts)     
#with open(home + '\\filelist.csv' , 'w',  encoding='utf-8') as derp:
#    writer = csv.writer(derp)
#    writer.writerows(dir_counts)
