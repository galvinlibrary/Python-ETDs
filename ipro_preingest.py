import os
import shutil
from shutil import copyfile

def string_replace(x):
    with open(x, encoding="utf8") as f:
        newText=f.read().replace('</title>', ": " + i + "</title>")
    
    with open(x, 'w', encoding="utf8") as f:
        f.write(newText)

srcDir = "C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\ipro_pruned"

for root, dirs, files in os.walk(srcDir):
    for d in dirs:
        for root, dirs, files in os.walk(srcDir + "\\" + d):
            my_list = []
            for f in files:
                if f == "mods.xml":
                    pass
                else:
                    my_list.append(os.path.splitext(f)[0])
                    #print(d, os.path.splitext(f)[0])
        #print(my_list)
        for i in my_list:
            # Build xml files for each item in list
            copyfile(srcDir + "\\" + d + "\\mods.xml", srcDir + "\\" + d + "\\" + i + ".xml")
            #print(d, i)
        
        
        # insert string before </title>
        for i in my_list:
            longname = (srcDir + "\\" + d + "\\" + i + ".xml")
            #print(longname)
            print(d, i)
            string_replace(longname)
        #string_replace(i)
        # delete mods.xml
        
        # zip that shit.
