#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import authenticate
from errors import alert_message


params = FieldStorage()

if (environ['REQUEST_METHOD'].upper() == 'POST'):
    user = {
        'username': params.getvalue('username'),
        'password': params.getvalue('password')
    }
    
    success, user_id = authenticate(user)   # user_id is for session later on
    
    if success:
        print('Location: upload_page.py')


print('''
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
                    <h2>LOGIN</h2>
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
                    <input type="submit" name="buttonRedirect" value="Login"/>
                </div>
                <div>
                    <label>Not registered?</label>
                    <a href="register_page.py">Register</a>
                </div>
                <div>
                    <label>Forgot password?</label>
                    <a href="change_password_page.py">Reset password</a>
                </div>
            </form>''')

if (environ['REQUEST_METHOD'].upper() == 'POST') and (not success):
    print(f'<script>alert("Login failed!\\n{alert_message["l"]}");</script>')

print('''</body>
        </html''')


