import os
import shutil


srcDir = "C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\ipro"

dest =  "C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\ipro_pruned"

for root, dirs, files in os.walk(srcDir):
    for d in dirs:
        #print(d)
        newdir = (dest + "\\" + d)
        #print(newdir)
        if not os.path.exists(newdir):
            os.mkdir(newdir)
        for root, dirs, files in os.walk(srcDir + "\\" + d):
            #print(files)
            for file in files:
                if file[-4:].lower() == '.pdf':
                   shutil.copy(os.path.join(root, file), os.path.join(dest + "\\" + d, file))
                    #print(dest + "\\" + d + "\\" + file)        
                if (root + "\\" + "mods.xml"):
                    print("mods exists")
                    #shutil.copy((root + "\\" + "mods.xml"), os.path.join(dest + "\\bags\\" + d + "mods.xml"))
                    shutil.copy((root + "\\" + "mods.xml"), os.path.join(dest + "\\" + d + "\\mods.xml"))
