from bs4 import BeautifulSoup

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close 
    return data


soup = BeautifulSoup(read_file(),'lxml') 

title = soup.title

parent = title.parent

# .parents - returns a list of parents
link = soup.a
for parent in link.parents:
    print(parent.name)