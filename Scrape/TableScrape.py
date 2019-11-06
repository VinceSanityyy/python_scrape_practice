import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
# url = "https://twitter.com/realdonaldtrump"

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page,'lxml')
    return soupdata

playerdata = playerdatasaved = ""
for letter in ascii_lowercase:
    soup = make_soup('https://www.basketball-reference.com/players/'+letter+'/')
    for record in soup.findAll('tr'):
        playerdata = ""
        for data in record.findAll(['td','th']):
            playerdata = playerdata+','+data.text
        if len(playerdata)!= 0:
            playerdatasaved = playerdatasaved + '\n' +  playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,Colleges" 
file = open(os.path.expanduser('basketball.csv'),'wb')
file.write(bytes(header, encoding="ascii",errors="ignore"))
file.write(bytes(playerdatasaved, encoding="ascii",errors="ignore"))

print(playerdatasaved)


   # playername = ""
    # for data in record.findAll('th'):
    #      playername = playername+','+data.text+ ','

  