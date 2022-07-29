from flask_wtf import FlaskForm
from wtforms import DateField,IntegerField,SubmitField

class NewSession(FlaskForm):

    date = DateField('Todays Date:')
    session_set_order = IntegerField('Exercise order for todays workout:')
    
