import requests
import re
import json
from bs4 import BeautifulSoup
from pprint import pprint


url = requests.get("https://www.99.co/singapore/condos-apartments/a-treasure-trove?fbclid=IwAR1ofpfx4SR-vjKZSnrsP2Boa5nvqBCFaoGznjkyRK6Cv3ipdGcq72C4Hnw").text
soup = BeautifulSoup(url, 'html.parser')

tag = soup.find('script',text=re.compile('window.__data'))
tag = tag.get_text().split('floor_plan_map')[1].split('unit_config_items')[0]
url = []

for i in tag.split('"url":'):
    if 'https' in i:
        url.append(i.split(',"title"')[0].replace('\\u002F','/'))
pprint(url)

