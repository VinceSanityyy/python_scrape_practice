import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.99.co/singapore/condos-apartments/a-treasure-trove')

soup = BeautifulSoup(r.content,'lxml')
soup.find_all(r.content)

# print(soup)



g_data = soup.find_all('div',{'class': 'FloorPlans__controlItem__2VBHk'})
# print(g_data[0].text)
for item in g_data:
    #ignoreindex
    
    try:
        print(item.contents[0].text)
        print(item.contents[1].text)
        print(item.contents[2].text)
        # print(item.contents[1].find_all('p',{'class':'FloorPlans__controlItemTitle__2cRCA'})[0].text)
        # print(item.contents[0].find_all('p',{'class':'FloorPlans__controlItemTitle__2cRCA'})[0].text)
        # print(item.contents[0].find_all('h2',{'class':'css-1j9dxys e1xfvim30'})[0].text)
        # print(item.contents[0].find_all('p',{'class':'css-1echdzn e1xfvim31'})[0].text)
        # print(item.contents[0].find_all('p',{'class':'css-1xonkmu'})[0].text)
       
        print('\n')
    except:
        pass
   