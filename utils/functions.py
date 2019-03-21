import functools

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import session as user_session, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from utils import status_code



db = SQLAlchemy()
session = Session()


def init_ext(app):
    db.init_app(app=app)
    session.init_app(app=app)


def get_db_uri(database):
    user = database.get('USER')
    password = database.get('PASSWORD')
    host = database.get('HOST')
    port = database.get('PORT')
    name = database.get('NAME')
    db = database.get('DB')
    driver = database.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, name)


# 登录验证
def is_login(func):
    @functools.wraps(func)
    def check_status(*args, **kwargs):
        try:
            if 'user_id' in user_session:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('user.login'))
        except Exception as e:
            return redirect(url_for('user.login'))
    return check_status
