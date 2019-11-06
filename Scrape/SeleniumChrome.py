from selenium import webdriver
chrome_path = r"C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://vancouver.craigslist.org')
driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()

x = driver.find_elements_by_class_name('hdrlnk')
for xs in x:
    print(xs.text)

