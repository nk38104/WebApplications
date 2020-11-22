#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ


request_type = environ.get('REQUEST_METHOD', '')

form = FieldStorage()

if(environ['REQUEST_METHOD'].upper() == 'POST'):
    print('Location: login_page.py')

print('''
       <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <h1>Upload Page</h1>
            <div>
                <a href="login_page.py">Log out</a> 
            </div>
        </body>
        </html>''')


