#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
import mysql.connector
import json
from password_utils import hash_password


db_conf = {
    "host": "localhost",
    "user": "root",
    "passwd": "",
    "database": "authentication"
}


def get_database_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["database"]
    )
    return mydb


def create_user(user):
    hashed_password = hash_password(user['password'])
    # hash answer also
    
    mydb = get_database_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute("""INSERT INTO users (username, password, email, question, answer) 
                        VALUES (%s, %s, %s, %s, %s)""", (user['username'], hashed_password, user['email'], user['question'], user['answer']))
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 


def get_user(username):
    mydb = get_database_connection()
    
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users WHERE username="%s"', username)
    myresult = cursor.fetchone()
    
    mydb.close()
    return myresult


