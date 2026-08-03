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
import os

conn = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT"))
)

cursor = conn.cursor(dictionary=True)

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