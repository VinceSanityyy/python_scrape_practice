import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page,'lxml')
    return soupdata
i = 1
soup = make_soup('https://uwaterloo.ca')
for img in soup.findAll('img'):
    temp = img.get('src')
    if temp[:1] == '/':
        image = "https://uwaterloo.ca" + temp
    else:
        image = temp
    # print(image)
    nametemp = img.get('alt')
    if len(nametemp) ==0 :
        filename = str(i)
        i = i + 1
    else:
        filename = nametemp
    imgfile = open(filename + ".jpeg",'wb')
    imgfile.write(urllib.request.urlopen(image).read())
    imgfile.close()
