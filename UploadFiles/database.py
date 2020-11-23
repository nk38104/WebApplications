#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
import mysql.connector
import json
from hasher import hash_string
from errors import alert_status


db_conf = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'database': 'authentication'
}


def get_database_connection():
    mydb = mysql.connector.connect(
        host=db_conf['host'],
        user=db_conf['user'],
        passwd=db_conf['passwd'],
        database=db_conf['database']
    )
    return mydb


def create_user(user):
    hashed_password = hash_string(user['password'])
    hashed_answer = hash_string(user['answer'].lower())
    try:
        mydb = get_database_connection()
        cursor = mydb.cursor()
        cursor.execute("""INSERT INTO users (username, password, email, question, answer) 
                            VALUES (%s, %s, %s, %s, %s)""", (user['username'], 
                                                             hashed_password, 
                                                             user['email'], 
                                                             user['question'], 
                                                             hashed_answer))
        mydb.commit()
    except:
        return None
    return cursor.lastrowid


def get_user(username):
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
    my_result = cursor.fetchone()
    mydb.close()
    return my_result


def check_availability(username, email):
    try:
        mydb = get_database_connection()
        cursor = mydb.cursor()
        cursor.execute(f'SELECT * FROM users WHERE username="{username}"')
        username_result = cursor.fetchone()
        cursor.execute(f'SELECT * FROM users WHERE email="{email}"')
        email_result = cursor.fetchone()
        mydb.close()
    except:
        mydb.close()
        return alert_status['database_error']
    
    if (not username_result) and (not email_result):
        return alert_status['success']
    elif (username_result):
        return alert_status['username_exists']
    else:
        return alert_status['email_exists']


def change_user_password(username, password):
    hashed_password = hash_string(password)
    mydb = get_database_connection()
    cursor = mydb.cursor()
    cursor.execute(f'UPDATE users SET password="{hashed_password}" WHERE username="{username}"')
    mydb.commit()
    mydb.close()


