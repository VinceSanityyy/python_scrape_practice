import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page,'lxml')
    return soupdata


soup = make_soup('https://www.tripadvisor.com.ph/Hotel_Review-g187497-d1828529-Reviews-Catalonia_Barcelona_Golf-Barcelona_Catalonia.html#REVIEWS')
link = soup.find(attrs={'class':'ui_button nav next primary'})

for data in link:
    print(link.get('href'))