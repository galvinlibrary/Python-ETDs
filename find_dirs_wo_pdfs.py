import os
#import fnmatch
import glob

### This script separates the dspace ppp collection items into groups containing PDF and RIS objects

home = 'C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\ppp_pdf_simple'
#dest = 'C:\\Users\\tfluhr\\Desktop\\clean_dspace_exports\\ppp_ris'
dir_list = []

for dirs, subs, files in os.walk(home):
    #print(dirs)
    if glob.glob(dirs + "\\*.pdf"):
        print(dirs)
    else:
        print(dirs + " has no pdfs!")
