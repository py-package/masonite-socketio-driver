from dataclasses import dataclass


@dataclass
class SocketClient:
    userID: str
    address: str
    sessionID: str
    socketID: str
    connected: bool
    extra: str

    def to_json(self):
        return {
            "userID": self.userID,
            "address": self.address,
            "sessionID": self.sessionID,
            "socketID": self.socketID,
            "connected": self.connected,
            "extra": self.extra,
        }
