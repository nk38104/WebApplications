#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import register
from errors import alert_message, alert_status


params = FieldStorage()

if (environ['REQUEST_METHOD'].upper()) == 'POST':
    user = {
        'username': params.getvalue('username'),
        'password': params.getvalue('password'),
        'repeated_password': params.getvalue('repeated_password'),
        'email': params.getvalue('email'),
        'question': params.getvalue('question'),
        'answer': params.getvalue('answer')
    }
    
    success = register(user)
    
    if (success == alert_status['success']):
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
                    <h2>REGISTER</h2>
                </div>
                <div>
                    <label>Username</label>
                    <input type="text" name="username" placeholder="Enter username..."/>
                </div>
                <div>
                    <label>Password</label>
                    <input type="password" name="password" placeholder="Enter password..."/>
                </div>
                <div>
                    <label>Repeat password</label>
                    <input type="password" name="repeated_password" placeholder="Repeat password..."/>
                </div>
                <div>
                    <label>E-mail</label>
                    <input type="email" name="email" placeholder="Enter e-mail..."/>
                </div>
                <div>
                    <label>Secret question?</label>
                    <input type="text" name="question" placeholder="Enter question..."/>
                </div>
                <div>
                    <label>Answer</label>
                    <input type="text" name="answer" placeholder="Enter answer..."/>
                </div>
                <div>
                    <input type="submit" value="Register"/>
                </div>
            </form>''')

if (environ['REQUEST_METHOD'].upper() == 'POST') and (success != alert_status['success']):
    print(f'<script>alert("Registration failed!\\n{alert_message[success]}");</script>')

print("""</body>
        </html>""")


