import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)

with open("person.pkl", "wb") as f:
    pickle.dump(p, f)

with open("person.pkl", "rb") as f:
    person = pickle.load(f)

print(person.name, person.age)
