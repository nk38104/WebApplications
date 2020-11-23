#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import get_user_question
from errors import alert_message, alert_status
from hasher import verify_input
from database import change_user_password


params = FieldStorage()
stage = params.getvalue('submit')
error_msg = None

if (environ['REQUEST_METHOD'].upper()) == 'POST':
    user = {
        'username': params.getvalue('username'),
        'answer': params.getvalue('answer'),
        'password': params.getvalue('password'),
        'repeated_password': params.getvalue('repeated_password')
    }
    
    if(stage != None):
        stored_question, stored_answer = get_user_question(user)
    
        if(stored_question):
            if(stage == 'Reset') and (verify_input(stored_answer, user['answer'].lower())):
                if(user['password'] == user['repeated_password']):
                    change_user_password(user['username'], user['password'])
                    print('Location: login_page.py')
                else:
                    error_msg = alert_status['repeated_password_doesnt_match']
                    stage = 'Next'
            else:
                error_msg = alert_status['answer_doesnt_match']
        else:
            error_msg = alert_status['username_doesnt_exist']
            stage = None


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

if(stage == None):
    print('''
                    <div>
                        <label>Username</label>
                        <input type="text" name="username" placeholder="Enter username..."/>
                    </div>
                    <div>
                        <input type="submit" name="submit" value="Next"/>
                    </div>
                </form>''')

if(stage == 'Next'):
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
                        <input type="submit" name="submit" value="Reset"/>
                    </div>
                    <input type="hidden" name="username" value="{1}"/>
                </form>'''.format(stored_question, user['username']))

if (environ['REQUEST_METHOD'].upper() == 'POST') and (error_msg):
    print(f'<script>alert("Reset failed!\\n{alert_message[error_msg]}");</script>')

print('''
        </body>
        </html>''')


