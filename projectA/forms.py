from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , IntegerField 
from wtforms.validators import DataRequired, Email ,ValidationError , Length
from .models import User


class Register_form(FlaskForm):
    password = PasswordField('password : ', validators=[DataRequired(),Length(min=6,max=20)])
    email = StringField('email : ', validators=[DataRequired(), Email()])
    submit = SubmitField('Register Account')

    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email arleady taken !')

class Login_form(FlaskForm):
    email = StringField('email : ', validators=[DataRequired(), Email()])
    password = PasswordField('password : ', validators=[DataRequired(),Length(min=6,max=20)])
    submit = SubmitField('Login')
    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first() == None:
            raise ValidationError('your email dosent exsiste')

class Package_form(FlaskForm):
    package_name = StringField('package name : ', validators=[DataRequired()])
    c_version = IntegerField('current version : ',validators=[DataRequired()])
    f_version = IntegerField('force version : ',validators=[DataRequired()])