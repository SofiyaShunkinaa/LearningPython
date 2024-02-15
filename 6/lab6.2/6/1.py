import pickle

user = {
    'name': "Sofi",
    'age': 19,
    'email': "sofi@local.host"
}

with open('1.pickle', 'wb') as f:
    pickle.dump(user, f)

with open('1.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)

