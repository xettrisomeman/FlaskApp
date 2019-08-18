class BaseConfig(object):
     '''
     Base config class
    '''
     DEBUG = True
     TESTING = False


class ProductionConfig(BaseConfig):
     """
     Production specific config
     """
     DEBUG = False
     SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
     SQLALCHEMY_TRACK_MODIFICATIONS = False

    

class DevelopmentConfig(BaseConfig):
    """
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = True


