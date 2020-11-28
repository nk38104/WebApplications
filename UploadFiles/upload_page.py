#! C:\Users\Nikola Kelava\AppData\Local\Programs\Python\Python38-32\python.exe
from cgi import FieldStorage
import os


request_type = os.environ['REQUEST_METHOD']
params = FieldStorage()
img_dir_path = '../../../../htdocs/images'

if (not os.path.isdir(img_dir_path)): #inace ce vratiti gresku svaki put kad se post-a
    os.mkdir(img_dir_path)
 
images = os.listdir(img_dir_path)

if (request_type.upper() == 'POST'):
    file_item = params["image"]

    if (file_item.filename):
        img_dir_path = '../../../../htdocs/images/'
        img_dir_path += os.path.basename(file_item.filename)
        open(img_dir_path, 'wb').write(file_item.file.read(250000))
        message = f'The file "{img_dir_path}" is uploaded successfully.'
        success = True
    else:
        message = 'No file was uploaded'
        success = False
    
    # if (success):
    #     print('Location: upload_page.py')


print('''
       <!DOCTYPE html>
        <html>
        <head>
            <title>Upload Files</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                }
                img {
                    padding-right: 20px;
                }
                #image-container {
                    margin: 60px 350px 0 350px;
                }
                form {
                    margin-top: 120px;
                    text-align: center;
                }
                h1 {
                    text-align: center;
                }
                #logout {
                    margin-right: 25px;
                    margin-top: 10px;
                    font-size: 20px;
                    text-align: right;
                }
            </style>
        </head>
        <body>
            <nav>
                <div id="logout">
                    <a href="login_page.py">Log out</a>
                </div>
            </nav>
            <div>
                <h1>Upload Page</h1>
            </div>''')

print('''
        <form enctype="multipart/form-data" method="POST">
            <div id="upload_container">
                <input type="file" name="image" accept="image/png, image/jpeg">
                <input type="submit" name="upload" value="Upload">
            </div>
        </form>
        <div id="image-container">''')

for image in images:
    print(f'<img src="../../../../images/{image}" width=300 height=200 alt="{image}">')
    
if (request_type.upper() == 'POST') and (not success):
    print(f'<script>alert("Image upload failed!\\n{message}");</script>')

print('''</div>
        </body>
        </html>''')


