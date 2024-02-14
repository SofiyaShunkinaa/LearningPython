import re

text = "The quick brown fox jumps over the lazy fox."
result = re.sub(r'fox', 'dog', text)
print(result)
