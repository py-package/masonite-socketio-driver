from ...socketio_driver.communicator import Communicator


class SocketDriver:
    def __init__(self, application) -> None:
        self.application = application
        self.connection = None

    def set_options(self, options):
        self.options = options
        return self

    def get_connection(self):

        if self.connection:
            return self.connection

        self.connection = Communicator(
            {
                "host": self.options.get("host"),
                "port": self.options.get("port"),
            }
        )

        return self.connection

    def channel(self, channel, event, value):
        connection = self.get_connection()
        return connection.To(channel).Emit(event, value)

    def authorize(self, channel, socket_id):
        return self.get_connection().authenticate(channel=channel, socket_id=socket_id)
