from fastapi import FastAPI, HTTPException
from models import Student, UpdateStudent
from database import students_collection
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Student CRUD API",
    description="MongoDB Integration",
    version="1.0"
)

# Create Student
@app.post("/students")
def create_student(student: Student):
    existing_student = students_collection.find_one(
        {"email": student.email}
    )

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student with this email already exists."
        )

    result = students_collection.insert_one(
        student.dict()
    )

    return {
        "message": "Student Added Successfully",
        "id": str(result.inserted_id)
    }

# Read By Email
@app.get("/students/{email}")
def get_student(email: str):
    student = students_collection.find_one(
        {"email": email}
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "course": student["course"],
        "email": student["email"]
    }

# Read All Students
@app.get("/students")
def get_students():
    students = []

    for student in students_collection.find():
        students.append({
            "id": str(student["_id"]),
            "name": student["name"],
            "age": student["age"],
            "course": student["course"],
            "email": student["email"]
        })

    return students

# Static Files
app.mount(
    "/static",StaticFiles(directory="static"),
    name="static"
)

# Home Page
@app.get("/")
async def home():
    return FileResponse("static/index.html")