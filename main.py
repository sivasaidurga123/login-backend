from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

class Login(BaseModel):
    username:str
    password:str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9908706983",
    database="login_app"
)

cursor = connection.cursor(dictionary=True)

""" users=[
    {
        "username":"siva",
        "password":"123456"
    }
]
 """
@app.get("/")
def home():
    return{"message": "Hello Siva! Backend is working."}

@app.get("/about")
def about():
    return{
        " course" :"FastAPI",
        "student":"Siva"
}
@app.post("/login")
def login(user: Login):

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (user.username, user.password)
    )

    result = cursor.fetchone()

    if result:
        return {
            "status": "login successful"
        }

    return {
        "status": "Invalid information"
    }