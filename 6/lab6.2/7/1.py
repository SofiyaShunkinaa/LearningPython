import shelve

f = shelve.open('mydata.db')
f['name'] = "Alice"
f['age'] = 16
f['city'] = 'New York'
f.close()

f = shelve.open('mydata.db')
print(f['name'])