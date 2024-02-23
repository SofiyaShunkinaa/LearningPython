import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/home?hl=ru&gl=RU&ceid=RU:ru'
r = requests.get(url)
bs = BeautifulSoup(r.text, "html.parser")
text = bs.find('div', 'iNL53')
file = open('task1.txt', 'w')
file.write("Current temperature in Minsk: " + text.text)
print("Current temperature in Minsk: ", text.text)
file.close()