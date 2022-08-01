from dataclasses import dataclass


@dataclass
class SocketClient:
    userID: str
    address: str
    sessionID: str
    connected: bool
