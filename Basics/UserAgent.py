import requests
from fake_useragent import UserAgent

#background on user agents
ua = UserAgent()

header ={'user-agent':ua.chrome}

page = requests.get('https://www.google.com',headers=header)
print(page.content)

#timeout
page = requests.get('https://www.google.com',timeout = 3) 