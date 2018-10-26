import os
import shutil

home = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\unzipped'
multiple_pdfs = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\multiple_pdfs'

## get list of subdirectories
subs_list = []
def get_subs(home):
    
    for wd, subs, files in os.walk(home):
        subs_list.append(wd)
        
    del subs_list[0]
    #print(subs_list[0])


def find_multi(home):
    pdfs = (len([f for f in os.listdir(home)
    if f.endswith('.pdf') and os.path.isfile(os.path.join(home, f))]))
    return(pdfs)

get_subs(home)

for d in subs_list:
    if find_multi(d) == 1:
        print("one")
    else:
       shutil.move(d, multiple_pdfs)
    

#for d in subs_list:
#    if find_multi(d) == 2:
#        print("one file")
#    else:
#        print("KLASjdlJLSJD")
   
