import os
os.system('pip -qq install requests')
os.system('pip -qq install bs4')
os.system('pip -qq install pyfiglet')

import requests
import pyfiglet
from bs4 import BeautifulSoup

name = 'creativewiz'
print(pyfiglet.figlet_format(name, font='standard'))

url = input('Enter Url: ')
link = requests.get(url)
Soup_Obj = BeautifulSoup(link.content, 'html.parser')
print(Soup_Obj.prettify())