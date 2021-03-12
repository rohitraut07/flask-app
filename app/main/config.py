import os
import logging


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'sub'
    DATABASE_PASSWORD = '3366'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    TESTING = True


class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'sub'
    DATABASE_PASSWORD = '3366'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    TESTING = True


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_USER    : export user name              :       "root"
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export databse URI            :       dialect+driver://username:password@host:port/database
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_URI = os.environ.get("DATABASE_URI")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
