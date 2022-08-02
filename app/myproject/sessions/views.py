from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.sessions.forms import NewSession
from myproject.models import Sessions

sessions_blueprint = Blueprint('sessions',
                                __name__,
                                template_folder='templates/sessions')

@sessions_blueprint.route('/new_session_record',methods=['GET','POST'])
def new_session():


# @sessions_blueprint.route('/edit_session',methods=['GET','POST'])
# def edit_session():


# @sessions_blueprint.route('/view_')
# def view_session():
