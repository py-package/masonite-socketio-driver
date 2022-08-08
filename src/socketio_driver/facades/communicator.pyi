from ..models.socket_client import SocketClient

class Communicator:
    def clients() -> list[SocketClient]:
        """Returns a list of all clients."""
        ...
    def client(id: str) -> SocketClient | None:
        """Returns a client by id."""
        ...
    def delete(id: str) -> bool:
        """Deletes a client by id."""
        ...
    def delete_all_clients() -> None:
        """Deletes all clients."""
        ...
