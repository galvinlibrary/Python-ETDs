import os
import shutil
import csv

home = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\ppp'

dir_counts = []

for dirs, subs, files in os.walk(home):
    contents = os.listdir(dirs)
    count = len(contents)
    row = (dirs, count)
    dir_counts.append(row)
    
    #print(row)

print(dir_counts)     
with open('C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\ppp\\filelist.csv' , 'w',  encoding='utf-8') as derp:
    writer = csv.writer(derp)
    writer.writerows(dir_counts)
