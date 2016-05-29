import html2text
import os
import glob
import codecs
import csv
import sys
import re
from bs4 import BeautifulSoup

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

subject_terms = ["Drone", "Whistleblow", "Wiretap"]

article_list = []
article_names = []
for term in subject_terms:
    indir = "c:\\Users\\Sarah Hackney\\Desktop\\Indy Articles\\"+str(term)
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:



            try:

                with open(indir+"\\"+str(f), "r", encoding = "utf-8") as thisfile:


                    soup = BeautifulSoup(thisfile, "html.parser")

                    articletitle = soup.find_all("div", attrs = {"class" : "group-header"})
                    for title in articletitle:

                        namedate = title.text

                    articletext = soup.find_all("div", attrs = {"class" : "group-middle"})
                    for txt in articletext:

                        bodytext = txt.text


                    file = open(indir+"\\"+str(term)+"_"+str(f)+".txt", "w", encoding = "utf-8")
                    file.write(namedate + bodytext)





            except:
                continue
    # os.remove(glob.glob("c:\\Users\\Sarah Hackney\\Desktop\\Indy Articles\\"+str(term)+"\\"+"*.htm"))
