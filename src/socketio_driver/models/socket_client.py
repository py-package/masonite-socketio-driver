from dataclasses import dataclass


@dataclass
class SocketClient:
    id: str
    name: str
    address: str
