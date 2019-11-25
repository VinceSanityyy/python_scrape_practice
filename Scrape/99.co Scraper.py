import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.99.co/singapore/condos-apartments/a-treasure-trove')

soup = BeautifulSoup(r.content,'lxml')
soup.find_all(r.content)

# print(soup)


#parent div
g_data = soup.find_all('div',{'class': 'FloorPlans__controlItem__2VBHk'})

for item in g_data:
    #ignoreindex error
    try:
        print(item.contents[0].text)
        print(item.contents[1].text)
        print(item.contents[2].text)
    except:
        pass