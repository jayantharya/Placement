from pymongo import MongoClient

client = MongoClient("mongodb+srv://jkdarya:JkD1816@jkdarya.rbpb7ns.mongodb.net/")
db = client["My_Project"]

students = db["Trail"]



def add_student():
    