import certifi
from pymongo import MongoClient

client=MongoClient(
    "mongodb+srv://user_name:<password>@jkdarya.rbpb7ns.mongodb.net/",
    tlsCAFile=certifi.where()
)

db=client["studentdb"]
students_collection=db["students"]
