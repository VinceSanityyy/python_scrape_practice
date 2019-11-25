from selenium import webdriver
import urllib
import urllib.request
import string
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

chrome_path = r"C:\chromedriver.exe"

driver = webdriver.Chrome(chrome_path,options=options)
#total number of pages
pageNumber = 2324
#db connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='property_guru'
)

mycursor = mydb.cursor()

#loop pagination
for i in range(0,pageNumber,1):
    pageNumber = str(i)
   
    url = "https://www.propertyguru.com.sg/property-for-sale/"+pageNumber+"?order=desc&property_type=N&property_type_code%5B0%5D=CONDO&property_type_code%5B1%5D=APT&property_type_code%5B2%5D=WALK&property_type_code%5B3%5D=CLUS&property_type_code%5B4%5D=EXCON&sort=date"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')

    list_title = soup.select('.listing-card')
    # print(list_title)
    # time.sleep(15)
    driver.implicitly_wait(10)

    for q in list_title:
        name = q.find(attrs={'class':'nav-link'})
        location = q.find(attrs={'itemprop':'streetAddress'})
        listprice = q.find(attrs={'class':'list-price pull-left'})
        listAgent = q.find(attrs={'class':'agent-name'})
        agentPhone = q.find(attrs={'class':'listing-agent-phone-number'})
        var = name.attrs['title']
        firstAgentText = listAgent.text


        #FINAL VAR
        propName = var.replace('For Sale -', '')
        propLoc = location.text
        propPrice = listprice.text
        finalAgent = firstAgentText.replace('Listed by','')
        finalPhone = agentPhone.text

     
 
        print('record inserted')

        sql = """INSERT INTO guru_listings (property_name,property_address,property_price,listed_by,contact) VALUES (%s,%s,%s,%s,%s)"""
        mycursor.execute(sql,(propName,str(propLoc),str(propPrice),str(finalAgent),str(finalPhone)))
        mydb.commit()

        # time.sleep(5)

driver.close()


    