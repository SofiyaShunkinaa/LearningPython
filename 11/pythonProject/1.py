import requests
from bs4 import BeautifulSoup

url = 'https://yandex.by/pogoda/minsk?lat=53.902735&lon=27.555691'
r = requests.get(url)
bs = BeautifulSoup(r.text, "html.parser")
text = bs.find('span', 'temp__value temp__value_with-unit')
print(text.text)
