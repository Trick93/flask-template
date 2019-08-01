# config 全局配置文件

import datetime

#################pi################### flask设置 ##################################
DEBUG = True

#################################### MYSQL数据库设置 ##################################
DB_MYSQL_USER = 'root'                                                  # mysql数据库账号
DB_MYSQL_PASSWORD = 'root'                                              # mysql数据库密码
DB_MYSQL_HOST = 'localhost'                                             # mysql数据库ip
DB_MYSQL_PORT = 3306  # mysql数据库端口
DB_MYSQL_NAME = 'test'  # mysql数据库名称

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_MYSQL_USER + ":" + DB_MYSQL_PASSWORD + "@" + DB_MYSQL_HOST + "/" + DB_MYSQL_NAME

#################################### MONGODB数据库设置 ##################################
DB_MONGODB_USER = 'root'                                                # MongoDB数据库账号
DB_MONGODB_PASSWORD = 'root'                                            # MongoDB数据库密码
DB_MONGODB_NAME = 'test'                                                # MONGODB数据库名称
DB_MONGODB_HOST = 'localhost'                                           # MongoDB数据库ip
DB_MONGODB_PORT = 27017                                                 # MongoDB数据库端口

if DB_MONGODB_HOST and DB_MONGODB_PORT and DB_MONGODB_NAME:
    import pymongo

    Client = pymongo.MongoClient(DB_MONGODB_HOST, DB_MONGODB_PORT)
    DB_MONGODB = Client[DB_MONGODB_NAME]
    if DB_MONGODB_USER and DB_MONGODB_PASSWORD:
        Client.admin.authenticate(DB_MONGODB_USER, DB_MONGODB_PASSWORD, mechanism='SCRAM-SHA-1')

################################## JWT设置 ########################################
JWT_SECRET_KEY = '^!(@^&$(@#qazwsx'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=10)
JWT_TOKEN_LOCATION = 'cookies'
JWT_ACCESS_COOKIE_NAME = 'uuid'

################################## 其他设置 #######################################
LOG_PATH = './log/flask-stdout-log.log'
