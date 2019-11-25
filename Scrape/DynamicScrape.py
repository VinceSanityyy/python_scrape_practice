from bs4 import BeautifulSoup
import requests
from selenium import webdriver

chrome_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

res = ('https://www.hackerearth.com/challenges/')
driver.get(res)
res=driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

soup = BeautifulSoup(res,'lxml')

x = soup.find('div',{'class':'upcoming challenge-list'})
y = x.find_all('div',{'class':'challenge-card-modern'})
images = x.findAll('img')

img = driver.find_element_by_class_name('challenge-list-image challenge-card-wrapper')
# src = img.get_attribute('alt')

print(img)


# for i in y:
#     ctype = i.find('div',{'class':'challenge-type'}).text.replace('\n','').strip()
#     name = i.find('div',{'class':'challenge-name ellipsis dark'}).text.replace('\n','').strip()
#     date = i.find('div',{'class':'date less-margin dark'}).text.replace('\n','').strip()
#     image = img.get('src')

#     print(ctype,name,date)