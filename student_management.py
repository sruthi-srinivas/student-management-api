from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Student Management API")


# -----------------------------
# Pydantic Models
# -----------------------------

# Used when creating/updating a student
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    course: str = Field(..., min_length=1)
    age: int


# Used for the response
class Student(StudentCreate):
    id: int


# -----------------------------
# In-memory database
# -----------------------------

students = []

next_id = 1


# -----------------------------
# POST - Create Student
# -----------------------------

@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student_data: StudentCreate):

    global next_id

    student = Student(
        id=next_id,
        **student_data.model_dump()
    )

    students.append(student)

    next_id += 1

    return student


# -----------------------------
# GET - Get All Students
# -----------------------------

@app.get(
    "/students",
    response_model=list[Student]
)
def get_students():

    return students


# -----------------------------
# GET - Search Students by Course
# IMPORTANT: This must come BEFORE /students/{student_id}
# -----------------------------

@app.get(
    "/students/search",
    response_model=list[Student]
)
def search_students(course: str):

    result = []

    for student in students:

        if course.lower() in student.course.lower():
            result.append(student)

    return result


# -----------------------------
# GET - Get Student by ID
# -----------------------------

@app.get(
    "/students/{student_id}",
    response_model=Student
)
def get_student(student_id: int):

    for student in students:

        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# -----------------------------
# PUT - Update Student
# -----------------------------

@app.put(
    "/students/{student_id}",
    response_model=Student
)
def update_student(
    student_id: int,
    student_data: StudentCreate
):

    for index, student in enumerate(students):

        if student.id == student_id:

            updated_student = Student(
                id=student_id,
                **student_data.model_dump()
            )

            students[index] = updated_student

            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# -----------------------------
# DELETE - Delete Student
# -----------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            students.pop(index)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )