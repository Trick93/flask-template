# 该文件主要用于初始化整个个 flask 程序

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import platform
from logging import handlers

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    from app.url import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)

    from flask_jwt_extended import JWTManager
    JWTManager(app)

    # 日志记录格式初始化
    from app.config import LOG_PATH
    if platform.system() != "Windows":
        format_str = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s') #设置日志格式
        fileshandle = handlers.TimedRotatingFileHandler(LOG_PATH, when='midnight', interval=1, backupCount=8)
        fileshandle.suffix = "%Y-%m-%d.log"
        fileshandle.setFormatter(format_str)
        fileshandle.setLevel(logging.INFO)
        app.logger.addHandler(fileshandle)

    return app
