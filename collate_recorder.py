from lxml import etree
import glob
import csv
import pprint
import os,json

c = csv.writer(open("recorder_2000.csv","a"))
c.writerow(["Name","Filename","Text"])

for cr_file in glob.iglob('2000/*.xml'):
    ## I put this script in the folder above the folder containing the parsed files which was named 2000. Change the part in the parentheses before the slash to match the folder you want it to look through.
    try:
        tree = etree.parse(cr_file)
        for node in tree.iter('recorder'):
            c.writerow([node.attrib,cr_file,node.text])
    except:
        print "bad string" + " " + cr_file
        continue
        

        
