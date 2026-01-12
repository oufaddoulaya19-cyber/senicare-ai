from database import users

user = {
    "nom": "Benali",
    "prenom": "Ahmed",
    "age": 68,
    "email": "ahmed@gmail.com",
    "maladies": ["diabète", "hypertension"],
    "allergies": ["pénicilline"]
}

result = users.insert_one(user)

print("User inserted with ID:", result.inserted_id)
