from bs4 import BeautifulSoup

def read_file():
    file = open('intro-to-soup-html.html')
    data = file.read()
    file.close
    return data

#make soup



html_file = read_file()
soup = BeautifulSoup(html_file,'lxml')

print(soup.prettify())