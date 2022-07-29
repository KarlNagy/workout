from myproject import db
from sqlalchemy.dialects import mysql



class Exercises(db.Model):

    __tablename__ = 'exercises'
    id = db.Column(db.Integer,primary_key=True)
    program = db.Column(db.VARCHAR(75))
    exercise_name = db.Column(db.VARCHAR(75))
    measurable_type = db.Column(db.VARCHAR(20))
    focus = db.Column(db.VARCHAR(45))
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    form_reference = db.Column(db.Text(500))

    sessions = db.relationship('Sessions', backref='sessions')
    intensity = db.relationship('Intensity',backref='intensity')

    def __init__(self,program,exercise_name,measurable_type,focus,min,max,form):
        self.program = program
        self.exercise_name = exercise_name
        self.measurable_type = measurable_type
        self.focus = focus
        self.min = min
        self.max = max
        self.form_reference = form_reference


class Sessions(db.Model):

    __tablename__ = 'sessions'
    date = db.Column(db.Date,primary_key=True)
    session_set_order = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),primary_key=True)
    cycle_week = db.Column(db.Integer,nullable=True)
    exercise_id = db.Column(db.Integer,db.ForeignKey('exercises.id'))
    set = db.Column(db.Integer)
    lbs_added = db.Column(db.DECIMAL(4,1))
    measureable = db.Column(db.Integer)
    notes = db.Column(db.Text(500),nullable=True)

    def __init__(self,date,session_set_order,user_id,cycle_week,exercise_id,set,lbs_added,measureable,notes):
        self.date = date
        self.session_set_order = session_set_order
        self.user_id = user_id
        self.cycle_week = cycle_week
        self.exercise_id = exercise_id
        self.set = set
        self.lbs_added = lbs_added
        self.measureable = measureable
        self.notes = notes


class Users(db.Model):

    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(45))
    first_name = db.Column(db.VARCHAR(45))
    last_name = db.Column(db.VARCHAR(45))

    sessions = db.relationship('Sessions',backref='sessions')

    def __init__(self,email,password,first_name,last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


class Intensity(db.Model):

    __tablename__ = 'intensity'
    exercise_id = db.Column(db.Integer,db.ForeignKey('exercises.id'),primary_key=True)
    intensity_level = db.Column(db.Integer)

    def __init__(self,exercise_id,intensity_level):
        self.exercise_id = exercise_id
        self.intensity_level = intensity_level

db.create_all()