import os
from flask import current_app as app

class FileHandler():

    def save():
        raise NotImplementedError()

    def retrieve():
        raise NotImplementedError()


class LocalFileHandler(FileHandler):

    def save(file, file_name):
        file_path  = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)
    
        
    def retrieve(file_name):
        file = open(os.path.join(app.config['UPLOAD_FOLDER'], file_name), 'rb')
        return file



class S3FileHandler(FileHandler):

    def save(file, file_name):
        pass


    def retrieve(file_name):
        pass
