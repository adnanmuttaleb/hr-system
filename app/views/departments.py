from flask_restplus import Namespace, Resource, marshal_with
from flask import request
from flask_restplus import fields

from ..helpers import is_admin
from ..models import Department
from .. import db

api = Namespace('departments', description='Departments API',)

department_model = api.model('Department', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),

})

@api.route('/')
class DepartmentList(Resource):

    @marshal_with(department_model)
    def get(self):
        return Department.query.all()        
    
    @is_admin
    @api.expect(department_model, validate=False)
    def post(self):
        name = request.json["name"]
        department = Department(name=name)
        
        db.session.add(department)
        db.session.commit()

        return '', 200





        





