import urllib2
import urllib
import json
import urlparse
import os

save_path='C:\Users\LaurinParadise\Documents\Pratt\DigitalHumanities\PythonStuffForCongress\EdgarHoover'
## this is where you want the files saved
def main():
    with open("edgarhoover.txt","r") as f:
	##the part in the "" is the file containing the URLs that you've amassed, place this file within the same folder as the text file
        for x in f:
            urlParts = urlparse.urlsplit(x.strip())
            filename = urlParts.path.split('/')[-1]
            urllib.urlretrieve(x.strip(), os.path.join(save_path, filename))

if __name__ == "__main__":
    main()