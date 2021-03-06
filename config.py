import os
import logging
from dotenv import load_dotenv


class Config:
    load_dotenv(verbose=True)

    APP_NAME = 'Boiler-Plate-Python'
    SECRET_KEY = 'secret-key'
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 3000))

    LOG_PATH = os.environ.get('LOG_PATH', '/var/log/python-app.log')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'session_cookie')
    DB_CONNECTION_STRING = os.environ.get('DB_CONNECTION_STRING')


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    LOG_LEVEL = logging.DEBUG
    DB_CONNECTION_STRING = os.environ.get('TEST_DB_CONNECTION_STRING')


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.ERROR
