from selenium import webdriver
import mysql.connector
import csv
import os
import urllib
import urllib.request

max_page_num = 3000

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='scrape-data'
)

mycursor = mydb.cursor()
# print(mydb)

with open('products.csv', 'w', newline='',encoding='utf-8') as f:
    f.write('Name \n')

chrome_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
# driver.get('https://vancouver.craigslist.org/search/ela?s=0')


for i in range(0, max_page_num,120):
    # page_num =(max_page_digit - len(str(i))) + str(i)
    # page_num = (max_page_digit - len(str(i))) * '0' + str(i)
    page_num = str(i)
    # print(page_num)

    url = 'https://vancouver.craigslist.org/search/ela?s='+ page_num + ''
    driver.get(url)
   


    x = driver.find_elements_by_class_name('hdrlnk')
    y = driver.find_elements_by_xpath('//p[@class="result-info"]/span[@class="result-meta"]//span[@class="result-price"]')
    # images = driver.find_elements_by_xpath('//*[@id="sortable-results"]/ul/li/a/img')
    images = driver.find_elements_by_tag_name('img')
    # images = driver.find_elements_by_xpath('//li[@class="result-row"]/a[@class="result-image gallery"]//img[@class=""]')
    for i, image in enumerate(images):
        asdf = image.get_attribute("src")
        prod = (x[i].text)
        price = (y[i].text)
        print("prod", prod, "price", price, "image", asdf)
        
    #   for i in range(len(x)):
    #     asdf = img.get_attribute("src")
    #     prod = (x[i].text)
    #     price = (y[i].text)
    #     image = asdf
    #     print("prod", prod, "price", price, "image", image)
        # sql =  """INSERT INTO products (name,price,image) VALUES (%s,%s,%s)"""
        # mycursor.execute(sql,(prod,price,image))
        # mydb.commit()


   
driver.close()