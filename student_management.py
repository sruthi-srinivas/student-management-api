from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Student Management API")


# =====================================================
# PYDANTIC MODELS
# =====================================================

# Used for creating and updating a student
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    course: str = Field(..., min_length=1)
    age: int


# Used for API responses
class Student(StudentCreate):
    id: int


# =====================================================
# IN-MEMORY DATABASE
# =====================================================

students = []

next_id = 1


# =====================================================
# POST - CREATE STUDENT
# =====================================================

@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student_data: StudentCreate):

    global next_id

    # Check if student already exists
    for student in students:

        if student.email.lower() == student_data.email.lower():

            raise HTTPException(
                status_code=400,
                detail="Student already exists"
            )

    # Create new student
    student = Student(
        id=next_id,
        **student_data.model_dump()
    )

    students.append(student)

    next_id += 1

    return student


# =====================================================
# GET - GET ALL STUDENTS
# =====================================================

@app.get(
    "/students",
    response_model=list[Student]
)
def get_students():

    return students


# =====================================================
# GET - SEARCH STUDENTS BY COURSE
# IMPORTANT:
# This route must come BEFORE /students/{student_id}
# =====================================================

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


# =====================================================
# GET - GET STUDENT BY ID
# =====================================================

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


# =====================================================
# PUT - UPDATE STUDENT
# =====================================================

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

            # Check if email belongs to another student
            for existing_student in students:

                if (
                    existing_student.email.lower()
                    == student_data.email.lower()
                    and existing_student.id != student_id
                ):

                    raise HTTPException(
                        status_code=400,
                        detail="Email already exists"
                    )

            # Create updated student
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


# =====================================================
# DELETE - DELETE STUDENT
# =====================================================

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