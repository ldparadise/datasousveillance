import csv
import glob
import ast
from os.path import isfile
from lxml import etree

def look_for_speaker_in_files(speakerAttrib):
    speakerDict = ast.literal_eval(speakerAttrib)
    file_name = str(speakerDict.values()[0]).format()
    l_file_exists = False
    if isfile(file_name + "_2000.csv"):
        l_file_exists = True
    c = csv.writer(open(file_name + "_2000.csv","a"))
    ## this and line 11 are going to name the file the speaker name as it appears, like "MR. PAUL" + whatever you put before the .csv
	## The _2000 was because we were making the year part of the naming convention	
    lparser = etree.XMLParser(recover=True)
    for cr_file in glob.iglob('2000/*.xml'):
	## change what is in parentheses before the slash to match the folder that you want the program to look through.
        try:
          tree = etree.parse(cr_file,parser=lparser)
          for node in tree.iter('speaking'):
             if node.keys() == speakerDict.keys():
                if node.values() == speakerDict.values():
                    c.writerow([node.attrib, cr_file, node.text])
                else:
                    continue
             elif 'quote' in node.attrib:
                 if file_name in node.values():
                     c.writerow([node.attrib, cr_file, node.text])
                     print "found quote"
                 else:
                     continue
             else:
                 continue
        except:
          print "bad string " + cr_file
          raise

def main():
    with open("speaking2000.txt","r") as speaker_list:
	## this is the file that contains the speaker list as you've generated or the speakers you are looking for.
        for x in speaker_list:
            print x
            look_for_speaker_in_files(x)
if __name__ == "__main__":
    main()




