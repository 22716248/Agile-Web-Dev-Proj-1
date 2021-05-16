from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, DataRequired, EqualTo
from app.models import User, Score

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class QuizForm(FlaskForm):
    
    question1 = StringField("Question 1: ", validators=[DataRequired()])
    question2 = StringField("Question 2: ", validators=[DataRequired()])
    question3 = StringField("Question 3: ", validators=[DataRequired()])
    question4 = StringField("Question 4: ", validators=[DataRequired()])
    question5 = StringField("Question 5: ", validators=[DataRequired()])
    question6 = StringField("Question 6: ", validators=[DataRequired()])
    question7 = StringField("Question 7: ", validators=[DataRequired()])
    question8 = StringField("Question 8: ", validators=[DataRequired()])
    question9 = StringField("Question 9: ", validators=[DataRequired()])
    question10 = StringField("Question 10: ", validators=[DataRequired()])

    submit = SubmitField('Submit Answers.')

def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')