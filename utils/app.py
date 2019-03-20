
from flask import Flask

from utils.settings import template_dir, static_dir
from utils.functions import init_ext

from app.user_views import user_blueprint


# 定义函数，创建flask对象app
def create_app(config):
    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

    app.config.from_object(config)
    # 初始化对象
    init_ext(app)

    return app
