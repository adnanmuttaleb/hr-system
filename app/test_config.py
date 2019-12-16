import os
from pydoc import locate

APP_DIR =  os.path.dirname(__file__)
MIGRATIONS_DIR = os.path.join(APP_DIR, 'migrations')
BASE_DIR =  os.path.dirname(APP_DIR)

FILE_HANDLER = locate('app.file_utils.LocalFileHandler')
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"