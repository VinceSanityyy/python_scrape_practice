from bs4 import BeautifulSoup

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close 
    return data


soup = BeautifulSoup(read_file(),'lxml') 

title = soup.title

parent = title.parent



#parent
p = soup.p
print(p.parent.name)

#html
html = soup.html
print(type(html.parent)) 
