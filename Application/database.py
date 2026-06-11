import certifi
from pymongo import MongoClient

client=MongoClient(
    "mongodb+srv://jkdarya:JkD1816@jkdarya.rbpb7ns.mongodb.net/",
    tlsCAFile=certifi.where()
)

db=client["studentdb"]
students_collection=db["students"]
