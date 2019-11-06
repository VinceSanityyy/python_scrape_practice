from bs4 import BeautifulSoup

def read_file():
    file = open('tags.html')
    data = file.read()
    file.close
    return data

soup = BeautifulSoup(read_file(),'lxml')

meta = soup.meta


body = soup.body
body['style'] = 'asdf'


print(body['style'])

