from selenium import webdriver
import urllib
import urllib.request
import string
from bs4 import BeautifulSoup
import mysql.connector


chrome_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


#total number of pages
pageNumber = 2596
#db connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='stackoverflow_questions'
)

mycursor = mydb.cursor()

#loop pagination
for i in range(1,pageNumber,1):
    pageNumber = str(i)
    url = 'https://stackoverflow.com/questions/tagged/laravel?tab=newest&page='+pageNumber+'&pagesize=50'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')

    question_title = soup.select('.question-summary')

    for q in question_title:
        question = q.select_one('.question-hyperlink').getText()
        tags = q.select_one('.tags').getText()
        tags_with_comma = tags.replace(' ', ',')
        vote_count = q.select_one('.vote-count-post').getText()
        status = q.select_one('.status').getText()
        answercount = status[1]

        sql = """INSERT INTO questions (title,tags,vote_count,answer_count) VALUES (%s,%s,%s,%s)"""
        mycursor.execute(sql,(question,str(tags_with_comma),str(vote_count),str(answercount)))
        mydb.commit()
        print('record inserted')

driver.close()


    