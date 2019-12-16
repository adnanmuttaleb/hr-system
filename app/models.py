from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import desc
from . import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    years_of_exp = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    resume_filename = db.Column(db.String(100))

    department_id = db.Column(
        db.Integer, 
        db.ForeignKey('department.id'),
        nullable=False
    )

    department = db.relationship(
        'Department', 
        backref=db.backref('candidates', lazy=True)
    )
    
    registration_date = db.Column(db.DateTime, default=datetime.now)
    
    @staticmethod
    def get_candidates():
        return Candidate.query.order_by(desc(Candidate.registration_date)).all() 

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False)




