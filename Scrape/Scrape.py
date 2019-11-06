import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.nytimes.com/section/politics')

soup = BeautifulSoup(r.content,'lxml')
soup.find_all(r.content)

links = soup.find_all('a')

for link in links:
    # print (link.text,link.get('href'))
    # print("<a href = '%s'>%s</a>"%(link.get("href"),link.text))
    pass



g_data = soup.find_all('div',{'class': 'css-1l4spti'})
for item in g_data:
    #ignoreindex
    try:
        print(item.contents[0].find_all('h2',{'class':'css-1j9dxys e1xfvim30'})[0].text)
        print(item.contents[0].find_all('p',{'class':'css-1echdzn e1xfvim31'})[0].text)
        print(item.contents[0].find_all('p',{'class':'css-1xonkmu'})[0].text)
       
        print('\n')
    except:
        pass
   