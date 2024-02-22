#configuraciones a Base de datos 

import os 
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'Inali'
    SESSION_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:InaliQ01_21@127.0.0.1/bdFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False