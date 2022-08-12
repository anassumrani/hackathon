from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length

class customer_form(FlaskForm):
    forename = StringField('Enter Forename',validators=[DataRequired(), Length(min=1, max=50)])
    surname = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    address = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Enter Surname',validators=[DataRequired(), Length(min=1, max=50)])
    submit=SubmitField('Submit')

class assign_driver_form(FlaskForm):
    customer = SelectField('Customer', choices=[])
    driver =SelectField('Assign Driver', choices=[("Roy Chase","Roy Chase"),("Adam Smith","Adam Smith")],validators=[DataRequired()])
    submit = SubmitField('Submit')
