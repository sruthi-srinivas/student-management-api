# Student Management API

A simple REST API built using **FastAPI** to manage student records.

This project demonstrates **CRUD operations, Pydantic validation, HTTP methods, query parameters, path parameters, duplicate checking, and error handling**.

## 🚀 Features

* Create a new student
* Automatically generate student ID
* Get all students
* Get a student by ID
* Update a student
* Delete a student
* Search students by course
* Prevent duplicate student registration using email
* Validate email format
* Validate required fields using Pydantic
* Handle students that do not exist
* Interactive Swagger UI documentation

## 🛠️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Email Validator

## 📁 Project Structure

```text
student-management-api/
│
├── student_management.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sruthi-srinivas/student-management-api.git
```

### 2. Navigate to the project

```bash
cd student-management-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn student_management:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📚 Swagger UI

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all API endpoints interactively.

## 🔗 API Endpoints

| Method | Endpoint                      | Description               |
| ------ | ----------------------------- | ------------------------- |
| POST   | `/students`                   | Create a new student      |
| GET    | `/students`                   | Get all students          |
| GET    | `/students/search?course=CSE` | Search students by course |
| GET    | `/students/{student_id}`      | Get student by ID         |
| PUT    | `/students/{student_id}`      | Update a student          |
| DELETE | `/students/{student_id}`      | Delete a student          |

## 📝 Create a Student

### Request

```http
POST /students
```

### Request Body

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "course": "Python Full Stack",
  "age": 22
}
```

### Response

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "course": "Python Full Stack",
  "age": 22,
  "id": 1
}
```

The ID is generated automatically by the API.

## 🚫 Duplicate Student Check

The API checks whether the email already exists before creating a student.

If the same email is submitted again:

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "course": "Python Full Stack",
  "age": 22
}
```

The API returns:

```json
{
  "detail": "Student already exists"
}
```

Status code:

```text
400 Bad Request
```

## 🔍 Search Students by Course

Use:

```http
GET /students/search?course=CSE
```

The API searches students based on their course.

For example:

```json
[
  {
    "name": "Priya",
    "email": "priya@gmail.com",
    "course": "CSE",
    "age": 21,
    "id": 2
  }
]
```

## 🔎 Get Student by ID

Example:

```http
GET /students/1
```

If the student exists, the student details are returned.

If the student does not exist:

```json
{
  "detail": "Student not found"
}
```

Status code:

```text
404 Not Found
```

## ✏️ Update Student

Example:

```http
PUT /students/1
```

Request body:

```json
{
  "name": "Rahul Kumar",
  "email": "rahulkumar@gmail.com",
  "course": "FastAPI",
  "age": 23
}
```

The student's existing ID remains unchanged.

## 🗑️ Delete Student

Example:

```http
DELETE /students/1
```

Response:

```json
{
  "message": "Student deleted successfully"
}
```

## ✅ Input Validation

Pydantic validates the incoming request data.

The API checks:

* Name should not be empty
* Email should have a valid email format
* Course should not be empty
* Age should be an integer

Invalid input returns a validation error.

Example status code:

```text
422 Unprocessable Content
```

## 📌 HTTP Status Codes

| Status Code | Meaning                             |
| ----------- | ----------------------------------- |
| 200         | Successful request                  |
| 201         | Student created                     |
| 400         | Duplicate student / invalid request |
| 404         | Student not found                   |
| 422         | Validation error                    |

## 💾 Data Storage

Currently, the application uses an **in-memory Python list** to store student records.

This means all student data will be lost when the server is restarted.

For a production application, the in-memory list can be replaced with a database such as:

* PostgreSQL
* MySQL
* MongoDB

## 🎯 Learning Objectives

This project demonstrates:

* FastAPI application development
* REST API design
* CRUD operations
* GET, POST, PUT, and DELETE methods
* Path parameters
* Query parameters
* Pydantic models
* Request validation
* Email validation
* Duplicate data checking
* HTTP status codes
* Exception handling
* Swagger API testing

## 👩‍💻 Author

**Sruthi Pasupula**

GitHub: https://github.com/sruthi-srinivas
