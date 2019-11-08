from selenium import webdriver
import mysql.connector
import csv

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
    # print(url)

    # driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()
    # driver.find_elements_by_class_name('result')

    x = driver.find_elements_by_class_name('hdrlnk')
    y = driver.find_elements_by_class_name('result-price')
   
    # with open('products.csv', 'a',newline='',encoding='utf-8') as f:
    #        for i in range(len(x)):
    #             f.write(x[i].text +'\n')
    for i in range(len(x)):
        prod = (x[i].text)
        sql =  """INSERT INTO products (name) VALUES (%s)"""
        mycursor.execute(sql,(prod,))
        mydb.commit()

    
   
driver.close()