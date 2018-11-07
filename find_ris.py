import os
import shutil

### This script separates the dspace ppp collection items into groups containing PDF and RIS objects

home = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\ppp'
dest = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\DSpaceUnproccessed\\ppp_ris'


for dirs, subs, files in os.walk(home):
    #print(files)
    for f in files:
        if f.endswith(".ris"):
            print(dirs)
            shutil.move(dirs, dest)
