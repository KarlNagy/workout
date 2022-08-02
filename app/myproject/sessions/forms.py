from flask_wtf import FlaskForm
from wtforms import DateField,IntegerField,SubmitField

class NewSessionRecord(FlaskForm):

    date = DateField('Todays Date:')
    session_set_order = IntegerField('Exercise order for todays workout:')
    cycle_week = IntegerField('Cycle Week')
    exercise_id = IntegerField('')






date = db.Column(db.Date,primary_key=True)
    session_set_order = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),primary_key=True)
    cycle_week = db.Column(db.Integer,nullable=True)
    exercise_id = db.Column(db.Integer,db.ForeignKey('exercises.id'))
    set = db.Column(db.Integer)
    lbs_added = db.Column(db.DECIMAL(4,1))
    measureable = db.Column(db.Integer)
    notes = db.Column(db.Text(500),nullable=True)
    
