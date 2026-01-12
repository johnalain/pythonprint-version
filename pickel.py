import pickle

data = {
    "username": "john",
    "age": 30,
    "skills": ["Python", "ML", "Data Science"]
}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
