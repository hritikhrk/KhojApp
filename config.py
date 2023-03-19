import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__name__))
print(basedir)

SECRET_KEY = os.environ.get('SECRET_KEY', 'secretkey')
MONGODB_URL = os.environ.get('MONGODB_URL', 'mongodb://localhost:27017')
UPLOAD_FOLDER = os.path.join(basedir, 'IMAGE_FILES')
print(UPLOAD_FOLDER)