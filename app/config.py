import os

class Config:
    
    SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://pitch:kavene2001@localhost/kavene'
    SECRET_KEY='1234'


class ProdConfig(Config):
   
    pass


class DevConfig(Config):
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}