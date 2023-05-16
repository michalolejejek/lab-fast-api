from fastapi import APIRouter
from .schema import *
from .storage import get_students
from pydantic import BaseModel

router = APIRouter()
students_db = get_students()


@router.post("/student/")
async def create_item(student: StudentUpdateSchema):
    return student


@router.get("/student/{student_id}")
async def get_student(student_id: int):
    if student_id in students_db:
        return students_db[student_id]


@router.put("/student/{student_id}")
async def update_student(student_id: int, student_data: StudentUpdateSchema):
    if student_id in students_db:
        students_db[student_id]["first_name"] = student_data.first_name
        students_db[student_id]["last_name"] = student_data.last_name
        return {"message": "Student updated successfully"}