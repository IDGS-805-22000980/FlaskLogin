import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False
    
class DevelopmentConfig(Config):
        DEBUG=True
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Eduardo26.@127.0.0.1/FlaskLogin'
        SQLALCHEMY_TRACK_MODIFICATIONS=False

