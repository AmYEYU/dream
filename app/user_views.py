from flask import Blueprint, render_template

from utils.functions import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')

@user_blueprint.route("/createdb/")
def create_db():
    db.create_all()
    return "创建成功"