import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="StrongPassword123",
        database="student_analyzer"
    )

