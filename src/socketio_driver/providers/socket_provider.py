""" A SocketProvider Service Provider"""

from masonite.packages import PackageProvider

from ..communicator import Communicator

from ..drivers.socket_driver import SocketDriver


class SocketProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (self.root("socketio_driver").name("socketio").config("config/socketio.py", publish=False))

    def register(self):
        super().register()
        self.application.bind("communicator", Communicator(self.application))
        self.application.make("broadcast").add_driver("socketio", SocketDriver(self.application))

    def boot(self):
        """Boots services required by the container."""
        pass
