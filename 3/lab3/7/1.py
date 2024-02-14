import re

text = "Я с 14.02.2024 по 15.02.2024 делаю лабы только по питону и не соображаю уже в "
result = re.findall(r'\d{2}.\d{2}.\d{4}', text)
print(result)

