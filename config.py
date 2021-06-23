import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://furcfmnbpmlmrs:a000a7abd4074c3d6a1ab3ec9d0b016e4e354cd33cdc03a03c2d3b6a2a093095@ec2-52-5-247-46.compute-1.amazonaws.com:5432/d1kg7e04599n7s'
    
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}