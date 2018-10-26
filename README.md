# Python-ETDs

Various scripts needed to prepare DSpace ETDs for islandora ingest.

###################
ETD Ingest Workflow
###################

1.  Export ETDs out of dspace via command line.
    - $ sudo ./dspace export --type=COLLECTION --id=65 --dest=/home/guru/ --number=1001 

2.  Run ziptest.py against the ETD export directory.  Be sure to check path variables.  This script will extract items from zip files         within each item export directory, move them to the parent directory and delete the zip file.

3.  Run multi.py against ETD export directory. Be sure to check path variables.  This script will separate ETDs into two groups. One           group containing items consisting of a single PDF file and another group containing items with multiple PDF files.  Multi-PDF items       will need to be manually inspected to merge or dispose extraneous PDFs.

4.  Run proquest.py against target ETD directory.  Be sure to check path variables. This script renames filename_DATA.xml file to             proquest.xml for xsl transform later.

5.  Run transforms.py against target ETD directory. Be sure to check path variables. This script runs Greer's three xsl transforms and         creates a mods.xml metadata file required for islandora ingest.  ****Before doing this remove subdirectory from Aldeman thesis (2276).     This is causing script to break and requires restarting the whole pipeline***

6.  Run dspace_preprocess.py against target ETD directory. Be sure to check path variables. This script renames mods.xml to match the         item.pdf filename and moves both the item.pdf and item.xml files to a completed directory. These files are now suitable for ingest         into islandora.


