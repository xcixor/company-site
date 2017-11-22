"""Creates the configurations for the app"""
class config:
    """
    Contains the configurations that all configuration options must have
    """
    @staticmethod
    def init_app(app):
        """To perform configuration specific initializations"""
        pass

class Development(config):
    """Configurations used during app development"""
    Debug = True

class Testing(config):
    """Configurations used for testing"""
    TESTING = True

#Registers the various configurations
config = {
    'development': Development,
    'testing': Testing,
    'default': Development
}
 