from bs4 import BeautifulSoup

def read_file():
    file = open('intro-to-soup-html.html')
    data = file.read()
    file.close 
    return data


soup = BeautifulSoup(read_file(),'lxml') 

title = soup.title
#print(title.string)

#replace func
title.string.replace_with('Changed')
print(title.string)