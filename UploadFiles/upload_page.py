#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
from os import environ, mkdir, path, listdir

request_type = environ['REQUEST_METHOD']
params = FieldStorage()
img_dir_path = '../../../../htdocs/images'

if (not path.isdir(img_dir_path)): # otherwise it returns error with every POST
    mkdir(img_dir_path)
 
images = listdir(img_dir_path)

if (request_type.upper() == 'POST'):
    file_item = params["image"]

    if (file_item.filename):
        img_dir_path = '../../../../htdocs/images/'
        img_dir_path += path.basename(file_item.filename)
        open(img_dir_path, 'wb').write(file_item.file.read(2500000))
        success = True
    else:
        message = 'No file was uploaded'
        success = False
    
    if (success):
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
                    height: 100vh;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    overflow: hidden;
                }
                nav {
                    border-bottom: 1px solid silver;
                }
                #nav-header {
                    text-align: center;
                    margin-left: 6%;
                    font-size: 30px;
                    color: white;
                }
                #nav-logout input {
                    float: right;
                    margin-top: 15px;
                    margin-right: 70px;
                    padding: 5px 15px;
                    font-size: 18px;
                    border: 1px solid silver;
                    border-radius: 5px;
                    background: linear-gradient(120deg, #2980b9, #8e44ad);
                    color: white;
                }
                #form-upload {
                    margin-left: 36%;
                }
                #form-upload form {
                    width: 500px;
                    margin-top: 120px;
                    padding: 10px;
                    text-align: center;
                    border: 3px solid white;
                    border-radius: 5px;
                }
                .txt-upload {
                    font-size: 18px;
                }
                img {
                    margin: 30px 20px;
                    border: 1px solid silver;
                    border-radius: 5px;
                }
                #image-container {
                    height: 510px;
                    margin: 70px 350px 0 350px;
                    border-bottom: 1px solid silver;
                    overflow: auto;
                }
            </style>
        </head>
        <body>
            <nav>
                <div id="nav-logout">
                    <form action="login_page.py" method="GET">
                        <input type="submit" value="Log out">
                    </form>
                </div>
                <div id="nav-header">
                    <h1>Upload Files</h1>
                </div>
            </nav>''')

print('''
            <div id="form-upload">
                <form enctype="multipart/form-data" method="POST">
                    <div id="upload_container">
                        <input class="txt-upload" type="file" name="image" accept="image/*">
                        <input class="txt-upload" type="submit" name="upload" value="Upload">
                    </div>
                </form>
            </div>
            <div id="image-container">''')

for image in images:
    print(f'<img src="../../../../images/{image}" width=350 height=200 alt="{image}">')
    
if (request_type.upper() == 'POST') and (not success):
    print(f'<script>alert("Image upload failed!\\n{message}");</script>')

print('''</div>
        </body>
        </html>''')


