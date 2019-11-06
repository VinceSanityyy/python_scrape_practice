import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/realdonaldtrump"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page,'lxml')

# print(soup.find('div',{'class':'ProfileHeaderCard'}).find('p').text)
i=1

for tweets in soup.findAll('div',{'class':'content'}):
    print(i)
    print(tweets.find('p').text)
    i = i+1

