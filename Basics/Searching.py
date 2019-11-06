from bs4 import BeautifulSoup
import re

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close
    return data

soup = BeautifulSoup(read_file(),'lxml')

#find
#find_all()

regex = re.compile('^b')
for tag in soup.find_all(regex):
    # print(tag.name)
    pass

regex = re.compile('t')
for tag in soup.find_all(regex):
    # print(tag.name)
    pass

#all a and b
for tag in soup.find_all(['a','b']):
    # print(tag.name)
    pass

def has_class(tag):
    return tag.has_attr('class')

for tag in soup.find_all(has_class):
    print(tag.name)
