import requests
from bs import BeautifulSoup

url = 'https://tech.onliner.by/'
r = requests.get(url)
print(r)