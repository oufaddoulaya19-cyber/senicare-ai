from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["senicare"]

users = db["users"]
chats = db["chats"]
messages = db["messages"]
medications = db["medications"]
emergency_contacts = db["emergency_contacts"]
email_logs = db["email_logs"]
