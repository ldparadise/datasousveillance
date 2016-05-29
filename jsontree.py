import os
import glob
import sys
import re
folders = ["api_Congress_70s", "api_Congress_Baseline", "api_Congress_2001", "api_Congress_2002", "api_Congress_2012", "api_Congress_2013", "api_Congress_2014", "api_Congress_2000", "api_Congress_Women", "api_Congress_A-D", "api_BerkeleyBarb", "api_FOXNews", "api_Indypendent", "api_MainstreamMedia", "api_PopCulture"]
filetext = []

for item in folders:
    indir = "C:\\Users\\Sarah Hackney\\Desktop\\APIJSON\\"+str(item)
    for root, dirs, filenames in os.walk(indir):
        for g in filenames:

            with open(indir+"\\"+str(g), "r", encoding = "utf-8") as f:

                for txt in f:

                    filetext = str(txt)
                f.close()

            file = open(indir+"\\"+"new_"+str(item)+"\\"+str(g), "w", encoding = "utf-8")
            file.write("{\"doc\": ")
            file.write(filetext)
            file.write("}")
