from masonite.providers import Provider
from . import MasoniteSocketioDriver

class MasoniteSocketioProvider(Provider):
    
    def __init__(self, application) -> None:
        self.application = application
        
    def register(self):
        self.application.make("broadcast").add_driver("socketio", MasoniteSocketioDriver(self.application))
    
    def boot(self):
        pass