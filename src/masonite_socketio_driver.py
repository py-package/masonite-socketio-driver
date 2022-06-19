class MasoniteSocketioDriver:

    def __init__(self, application) -> None:
        self.application = application
        self.connection = None

    def set_options(self, options):
        self.options = options
        return self

    def get_connection(self):
        try:
            from socket_io_emitter import Emitter
        except ImportError:
            raise ModuleNotFoundError(
                "Could not find the 'socket_io_emitter' library. Run 'pip install socket_io_emitter' to fix this."
            )

        if self.connection:
            return self.connection

        self.connection = Emitter({
            'host': self.options.get("host"),
            'port': self.options.get("port"),
        })

        return self.connection

    def channel(self, channel, event, value):
        connection = self.get_connection()
        return connection.To(channel).Emit(event, value)

    def authorize(self, channel, socket_id):
        return True
        # return self.get_connection().authenticate(channel=channel, socket_id=socket_id)
