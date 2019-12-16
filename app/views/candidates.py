from werkzeug.datastructures import MultiDict
from flask_restplus import Namespace, Resource, marshal_with
from flask import request
from flask_restplus import fields

from ..helpers import is_admin
from ..models import Candidate, Department
from ..forms import RegistrationForm
from .. import db

api = Namespace('candidates', description='Candidates API',)

department_model = api.model('Department', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),

})

candidate_model = api.model('Candidate', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'birth_date': fields.Date(required=True),
    'years_of_exp': fields.Integer(required=True),
    'department': fields.Nested(department_model)
})


candidate_creation_model = api.model('Candidate', {
    'name': fields.String(required=True),
    'birth_date': fields.Date(required=True),
    'years_of_exp': fields.Integer(required=True),
    'department': fields.Integer(),
})


@api.route('/')
class CandidateList(Resource):

    @is_admin
    @marshal_with(candidate_model)
    def get(self):
        return Candidate.get_candidates() 
    
    @api.expect(candidate_creation_model, validate=False)
    def post(self):
        form = RegistrationForm(MultiDict(mapping=request.json))
        if form.validate():
            candidate = Candidate(
                name=form.name.data, 
                years_of_exp=form.years_of_exp.data, 
                birth_date=form.birth_date.data,
                department=Department.query.get(form.department.data)
            )

            db.session.add(candidate)
            db.session.commit()

            return '', 200
        
        return form.errors, 400





        





