#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import authenticate
from errors import alert_message, alert_status


params = FieldStorage()

if (environ['REQUEST_METHOD'].upper() == 'POST'):
    user = {
        'username': params.getvalue('username'),
        'password': params.getvalue('password')
    }
    
    success, user_id = authenticate(user)   # user_id is for session later on
    error_msg = alert_status['incorrect_username_password']
    
    if success:
        print('Location: upload_page.py')


print('''
       <!DOCTYPE html>
        <html>
        <head>
            <title>Upload Files</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: Montserrat;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    height: 100vh;
                    overflow: hidden;
                }
                .container {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    width: 400px;
                    background: white;
                    border-radius: 10px;
                }
                .container h1 {
                    color: #666666;
                    text-align: center;
                    padding-bottom: 20px;
                    border-bottom: 1px solid silver;
                }
                .container form {
                    padding: 0 40px;
                    box-sizing: border-box;
                }
                form .txt_field {
                    position: relative;
                    border-bottom: 2px solid #adadad;
                    margin: 30px 0;
                }
                .txt_field input {
                    width: 100%;
                    padding: 0 5px;
                    height: 40px;
                    font-size: 16px;
                    border: none;
                    background: none;
                    outline: none;
                    color: #666666;
                }
                input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active {
                    -webkit-transition: "color 600s ease-out, background-color 600s ease-out";
                    -webkit-transition-delay: 600s;
                }
                .txt_field label {
                    position: absolute;
                    top: 50%;
                    left: 5px;
                    color: #adadad;
                    transform: translateY(-50%);
                    font-size: 16px;
                    pointer-events: none;
                    transition: .5s;
                }
                .txt_field span::before {
                    content: none;
                    position: absolute;
                    top: 40px;
                    left: 0;
                    width: 0%;
                    height: 2px;
                    background: #2691d9;
                    transition: .5s;
                }
                .txt_field input:focus ~ label,
                .txt_field input:valid ~ label {
                    top: -5px;
                    color: #2691d9;
                }
                .txt_field input:focus ~ span::before,
                .txt_field input:valid ~ span::before {
                    width: 100%;
                }
                .forgot_pass_link {
                    margin: -5px 0 20px 5px;
                    color: #a6a6a6;
                    cursor: pointer;
                }
                .forgot_pass_link a {
                    color: #2691d9;
                    text-decoration: none;
                }
                .forgot_pass_link:hover {
                    text-decoration: underline;
                }
                input[type="submit"] {
                    width: 100%;
                    height: 50px;
                    border: 1px solid;
                    background: #2691d9;
                    border-radius: 25px;
                    font-size: 18px;
                    color: white;
                    font-weight: 700;
                    cursor: pointer;
                    outline: none;
                }
                input[type="submit"]:hover {
                    border-color: #2691d9;
                    transition: .5s;
                }
                .register_link {
                    margin: 30px 0;
                    text-align: center;
                    font-size: 16px;
                    color: #666666;
                }
                .register_link a {
                    color: #2691d9;
                    text-decoration: none;
                }
                
                .register_link a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Login</h1>
                <form method="POST">
                    <div class="txt_field">
                        <input type="text" name="username" required/>
                        <span></span>
                        <label>Username</label>
                    </div>
                    <div class="txt_field">
                        <input type="password" name="password" required/>
                        <span></span>
                        <label>Password</label>
                    </div>
                    <div class="forgot_pass_link">
                        <a href="change_password_page.py">Forgot password?</a>
                    </div>
                    <input type="submit" name="btn_login" value="Login"/>
                    <div class="register_link">
                        Not registered? <a href="register_page.py">Register</a>
                    </div>
                </form>
            </div>''')

if (environ['REQUEST_METHOD'].upper() == 'POST') and (not success):
    print(f'<script>alert("Login failed!\\n{alert_message[error_msg]}");</script>')

print('''</body>
        </html''')


