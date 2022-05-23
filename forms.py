from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class  Comment_section(FlaskForm):
    username = StringField(label = "Username:", validators=[DataRequired(), Length(min=3, max = 30)])
    user_comment = TextAreaField(label = "Textarea:", validators=[DataRequired()])
    submit = SubmitField(label = "Submit")

class Register(FlaskForm):
    username =   StringField(label = "Username:", validators=[DataRequired(), Length(min=3, max = 30)])
    name =  StringField(label = "Name:", validators=[DataRequired(), Length(min=3, max = 30)])
    surname =  StringField(label = "Surname:", validators=[DataRequired(), Length(min=3, max = 30)])
    email =  StringField(label = "Email:", validators=[DataRequired(), Length(max = 30)])
    password =  StringField(label = "Password:", validators=[DataRequired(), Length(min=8, max = 30)])


class Login(FlaskForm):
    username =   StringField(label = "Username:", validators=[DataRequired(), Length(min=3, max = 30)])
    password =  StringField(label = "Password:", validators=[DataRequired(), Length(min=8, max = 30)])
