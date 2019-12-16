from wtforms import (
    Form, IntegerField, StringField, FileField,
    validators, DateField, ValidationError
)
from .models import Department

class RegistrationForm(Form):
    name = StringField('name', validators=[validators.DataRequired()])
    years_of_exp = IntegerField('years_of_exp', validators=[validators.DataRequired()])
    birth_date = DateField('birth_date', format='%d/%m/%Y', validators=[validators.DataRequired()])
    department = IntegerField('department', validators=[validators.DataRequired()])

    def validate_department(form, field):
        if not Department.query.get(field.data):
            raise ValidationError("Department Does Not exist")
