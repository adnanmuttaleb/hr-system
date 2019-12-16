import os
import uuid

from flask_restplus import Namespace, Resource, marshal_with
from flask import request, abort, send_file, current_app as app

from ..helpers import allowed_file, is_admin
from ..models import Candidate
from .. import db

api = Namespace('resume', description='Uploads API',)

@api.doc(params={"candidate_id": "Candidate ID"})
@api.route('/<int:candidate_id>')
class UploadResume(Resource):    

    def __init__(self, *args, **kwargs):
        super(UploadResume, self).__init__(*args, **kwargs)
        self.file_handler = app.config['FILE_HANDLER']

    def post(self, candidate_id):
        if 'file' not in request.files:
            abort(400, 'No file part' )      
        
        file = request.files['file']
        if file.filename == '':
            abort(400, 'No selected file')
        
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            abort(400, 'Candidate does not exist')

        if file and allowed_file(file.filename):
            filename = '{}.{}'.format(uuid.uuid4(), file.filename.split('.')[-1])
            self.file_handler.save(file, filename)
            candidate.resume_filename = filename
            db.session.commit()        
            
            return '', 200
        
        return 'Something went Wrong', 400


@api.doc(params={'candidate_id': "Candidate ID"})
@api.route('/<int:candidate_id>')
class DownloadResume(Resource): 

    def __init__(self, *args, **kwargs):
        super(DownloadResume, self).__init__(*args, **kwargs)
        self.file_handler = app.config['FILE_HANDLER']  
    
    @is_admin
    def get(self, candidate_id):
        print('here')
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            abort(404)

        resume = self.file_handler.retrieve(candidate.resume_filename)
        
        return send_file(
            resume, 
            as_attachment=True, 
            attachment_filename=os.path.basename(resume.name)
        )





        





