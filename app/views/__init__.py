from flask_restplus import Api
from .candidates import api as candidates_api
from .departments import api as departments_api
from .uploads import api as uploads_api

api = Api(
    title='HR For You',
    version='1.0',
    description='HR system RESTFul API',
)

api.add_namespace(candidates_api)
api.add_namespace(departments_api)
api.add_namespace(uploads_api)