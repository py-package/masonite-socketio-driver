from ..models.socket_client import SocketClient


class SocketDriver:
    def __init__(self, application) -> None:
        self.application = application
        self.connection = None
        self.client: SocketClient = None
        self.channels: list = []

    def set_options(self, options):
        self.options = options
        return self

    def get_connection(self):

        if self.connection:
            return self.connection

        self.connection = self.application.make("communicator")

        return self.connection

    def user(self, client: SocketClient):
        self.client = client
        return self

    def channels(self, channels):
        self.channels = channels
        return self

    def send(self, event, value):
        connection = self.get_connection()
        if self.client is not None:
            self.channel(self.client.socketID, event, value)
        elif len(self.channels) > 0:
            for channel in self.channels:
                self.channel(channel, event, value)
        else:
            connection.Emit(event, value)

        self.client = None
        self.channels = []

    def channel(self, channel, event, value):
        connection = self.get_connection()
        return connection.To(channel).Emit(event, value)

    def authorize(self, channel, socket_id, user_id):
        return self.get_connection().authenticate(
            channel=channel, socket_id=socket_id, user_id=user_id
        )
