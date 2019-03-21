from flask import render_template
from flask_script import Manager

from app.models import *
from utils.app import create_app
from utils.config import Config
from flask_migrate import Migrate,MigrateCommand
from utils.functions import db

# 创建flask对象app

app = create_app(Config)

# 使用Manager去管理falsk对象app
manage = Manager(app)

# Migrate 数据库迁移执行命令
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
