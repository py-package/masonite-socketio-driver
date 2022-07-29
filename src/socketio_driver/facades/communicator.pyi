from typing import Optional
from ..models.socket_client import SocketClient

class Communicator:
    def clients() -> list[SocketClient]:
        """Returns a list of all clients."""
        ...
    def client(id: str) -> SocketClient | None:
        """Returns a client by id."""
        ...
