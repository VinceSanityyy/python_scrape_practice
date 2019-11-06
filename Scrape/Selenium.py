from selenium import webdriver
import csv

max_page_num = 5
max_page_digit = 3

#create spreadsheet
with open('result.csv', 'w') as f:
    f.write('Buyers, Price \n')

driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.get('http://econpy.pythonanywhere.com/ex/001.html')

for i in range(1, max_page_num +1):
    page_num = (max_page_digit - len(str(i))) * '0' + str(i)
    url = 'http://econpy.pythonanywhere.com/ex/'+page_num+'.html'

    driver.get(url)
    # print(url)
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    header = "Buyer, Price" 
    page_items = len(buyers)
    with open('results.csv','a') as f:
        for i in range(page_items):
            f.write(buyers[i].text + ',' + prices[1].text + '\n')
driver.close

# #extract list buyer prices based xpath
# buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# #print buyers and prices in current page 
# page_items = len(buyers)
# # print(page_items)

# for item in range(page_items):
#     print(buyers[item].text + " : " + prices[1].text)

# #close driver
# driver.close()
