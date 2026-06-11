from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: EmailStr

class UpdateStudent(BaseModel):
    course: str | None=None
    age: int | None=None
    course: str | None=None
    email: EmailStr | None=None
