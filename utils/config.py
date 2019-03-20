
import redis
import os

from utils.settings import DATABASE, BASE_DIR
from utils.functions import get_db_uri


class Config(object):

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECREY_KEY = 'secret_key'

    SESSION_TYPE = 'redis'

    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379)

    SESSION_KEY_PREFIX = 'lyyc_'

    # 图片上传地址
    UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')
