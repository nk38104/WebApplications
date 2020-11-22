#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import get_user_question
from errors import alert_message, alert_status
from hasher import verify_input
from database import change_user_password


params = FieldStorage()
stage = alert_status['username']

if (environ['REQUEST_METHOD'].upper()) == 'POST':
    user = {
        'username': params.getvalue('username'),
        'answer': params.getvalue('answer'),
        'password': params.getvalue('password')
    }
    
    stage, user_record = get_user_question(user)
    
    if(user_record):
        question = user_record[4]
        if(user['answer'] != None):
            stored_answer = user_record[5]
            if(verify_input(stored_answer, user['answer'].lower())):
                change_user_password(user['username'], user['password'])
                print('Location: login_page.py')


print ('''
       <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                }
                form {
                    text-align: center;
                    margin-top: 150px;
                }
                caption {
                    padding-bottom: 50px;
                }
                input {
                    margin: 10px;
                }
                label {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <form method="POST">
                <div>
                    <h2>RESET PASSWORD</h2>
                </div>''')

if(stage == alert_status['username']):
    print('''
                    <div>
                        <label>Username</label>
                        <input type="text" name="username" placeholder="Enter username..."/>
                    </div>
                    <div>
                        <input type="submit" value="Next"/>
                    </div>
                </form>''')

if(stage == alert_status['question']):
    print('''
                    <div>
                        <label>Secret question?</label>
                        <input type="text" name="question" placeholder="{0}" disabled/>
                    </div>
                    <div>
                        <label>Answer</label>
                        <input type="text" name="answer" placeholder="Enter answer..."/>
                    </div>
                    <div>
                        <label>New password</label>
                        <input type="password" name="password" placeholder="Enter password..."/>
                    </div>
                    <div>
                        <label>Repeat password</label>
                        <input type="password" name="repeated_password" placeholder="Repeat password..."/>
                    </div>
                    <div>
                        <input type="submit" value="Reset"/>
                    </div>
                    <input type="hidden" name="username" value="{1}"/>
                </form>'''.format(question, user['username']))

if (environ['REQUEST_METHOD'].upper() == 'POST') and (stage != alert_status['question']):
    print(f'<script>alert("Registration failed!\\n{alert_message[stage]}");</script>')

print('''
        </body>
        </html>''')


