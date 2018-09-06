import os
import sys
import lxml.etree
import numpy
import shutil

home = "C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\test"

## xsl definitions

proquest_xsl = "C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\greer\\addproquest.xsl"
dc_xsl = "C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\greer\dc_to_mods_ir.xsl"
iit_xsl = "C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\greer\\mods_iitmetadata_combine.xsl"

## xml definitions

## get list of subdirectories
subs_list = []
def get_subs(home):
    
    for wd, subs, files in os.walk(home):
        subs_list.append(wd)
        
    del subs_list[0]
    #print(subs_list[0])
    
get_subs(home)

#print(subs_list)
for d in subs_list:
    # check for proquest.xml
    pq_found = d + "\\proquest.xml"
    if os.path.isfile(pq_found):
        local_pq_xsl = shutil.copy(proquest_xsl, d)
        new_dc = d + "\\dublin_core.xml"
        print("proquest file found")
        xml_input = lxml.etree.parse(d + "\\dublin_core.xml")
        xslt_root = lxml.etree.parse(local_pq_xsl)
        transform = lxml.etree.XSLT(xslt_root)
        derp = (str(transform(xml_input)))
        fd = open(new_dc, 'w', encoding="utf-8")
        fd.write(derp)
        # clean up
        fd.close()
        os.remove(local_pq_xsl)
        os.remove(pq_found)
    else:
        print("no proquest file found")
    ## run the dc to mods transform
    local_dc_xsl = shutil.copy(dc_xsl, d)
    new_mods = d + "\\temp_mods.xml"
    mods_xml_input = lxml.etree.parse(d + "\\dublin_core.xml")
    mods_xslt_root = lxml.etree.parse(local_dc_xsl)
    mods_transform = lxml.etree.XSLT(mods_xslt_root)
    mods_derp = (str(mods_transform(mods_xml_input)))
    mods_fd = open(new_mods, 'w', encoding="utf-8")
    mods_fd.write(mods_derp)
    mods_fd.close()
    ## run iit metadata transform
    if os.path.isfile(d + "\\metadata_iit.xml"):
        final_mods = d + "\\mods.xml"
        local_iit_xsl = shutil.copy(iit_xsl, d)
        print("iit metadata exists")
        iit_xml_input = lxml.etree.parse(d + "\\temp_mods.xml")
        iit_xml_root = lxml.etree.parse(local_iit_xsl)
        iit_transform = lxml.etree.XSLT(iit_xml_root)
        iit_derp = (str(iit_transform(iit_xml_input)))
        iit_fd = open(final_mods, 'w', encoding="utf-8")
        iit_fd.write(iit_derp)
    else:
       print("no iit metadata")
        