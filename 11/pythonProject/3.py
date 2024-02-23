import requests
from tkinter import *

facts = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1").json()

print(facts['text'])

