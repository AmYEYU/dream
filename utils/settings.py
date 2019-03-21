
import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态文件
static_dir = os.path.join(BASE_DIR, 'static')

# 模板文件
template_dir = os.path.join(BASE_DIR, 'templates')

# 数据库配置
DATABASE = {
    # 用户
    'USER': 'root',
    # 密码
    'PASSWORD': '123456',
    # 端口
    'PORT': 3306,
    # 主机地址
    'HOST': '127.0.0.1',
    # 数据库
    'DB': 'mysql',
    # 驱动 mysqlconnector pymysql
    'DRIVER': 'mysqlconnector',
    # 数据库名称
    'NAME': 'laoye'
}
