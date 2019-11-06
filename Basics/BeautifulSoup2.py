import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}
google = requests.get('https://www.google.com',headers = header)

soup = BeautifulSoup(google.content, 'lxml')
print(soup.prettify())