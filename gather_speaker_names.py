from lxml import etree
import glob
import csv
import pprint
import os,json

c = csv.writer(open("speaking2014.csv","w"))
## this names the file that you are putting all speaking tags into
c.writerow(["Name"])

for cr_file in glob.iglob('2014/*.xml'):
    ## I put this script in the folder above the parsed folder. The name of the folder you are parsing goes in the parentheses before the slash.
    try:
        tree = etree.parse(cr_file)
        for node in tree.iter('speaking'):
            c.writerow([node.attrib])
    except:
        print "bad string" + " " + cr_file
        continue
        

        
