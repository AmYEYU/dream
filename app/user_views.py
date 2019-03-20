from flask import Blueprint, render_template

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')