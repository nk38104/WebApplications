#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ
from authentication import authenticate


params = FieldStorage()

if (environ['REQUEST_METHOD'].upper() == 'POST'):
    if(params.getvalue('buttonRedirect') == 'Register'):
        print('Location: register_page.py')
    else:
        user = {
            'username' : params.getvalue("username"),
            'password' : params.getvalue("password")
        }
        
        success, user_id = authenticate(user)
        
        if not success:
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
                    <input type="submit" name="buttonRedirect" value="Register">
                </div>
            </form>''')

if (os.environ["REQUEST_METHOD"].upper() == "POST") and (not success):
    print('<script>alert("Incorrect username or/and password.\\nLogin failed!");</script>')

print("""</body>
        </html>""")