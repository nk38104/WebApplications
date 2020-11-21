#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ


request_type = environ.get('REQUEST_METHOD', '')

form = FieldStorage()

print('''
       <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <h1>Upload Page</h1>
        </body>
        </html>''')


