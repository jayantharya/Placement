from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://jkdarya:JKD1816@jkdarya.rbpb7ns.mongodb.net/")
db = client["My_Project"]
students = db["Trail"]

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: str

class UpdateStudent(BaseModel):
    email: str

@app.post("/students/")
def create_student(student_data: Student):
    student = {
        "name": student_data.name,
        "age": student_data.age,
        "course": student_data.course,
        "email": student_data.email
    }
    result = students.insert_one(student)
    return {"message": "Student created successfully!", "Student ID": str(result.inserted_id)}

@app.get("/students/")
def view_students():
    all_students = students.find()
    student_list = []
    for student in all_students:
        student["_id"] = str(student["_id"])
        student_list.append(student)
    return student_list

@app.delete("/students/{name}")
def delete_student(name: str):
    result = students.delete_one({"name": name})
    if result.deleted_count > 0:
        return {"message": "Student deleted successfully!"}
    else:
        raise HTTPException(status_code=404, detail="Student not found.")

@app.put("/students/{name}")
def update_student(name: str, update_data: UpdateStudent):
    new_email = update_data.email
    result = students.update_one({"name": name}, {"$set": {"email": new_email}})
    if result.modified_count > 0:
        return {"message": "Student updated successfully!"}
    else:
        raise HTTPException(status_code=404, detail="Student not found or email is the same.")