import requests


#requests.get(url) response object
response = requests.get('https://www.google.com')

#content
print(response.content)