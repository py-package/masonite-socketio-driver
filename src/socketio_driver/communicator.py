from masonite.configuration import config
import redis
import msgpack
from .models.socket_client import SocketClient


class Communicator:

    EVENT = 2
    BINARY_EVENT = 5

    def __init__(self, application):
        self.config = config("broadcast").get("broadcasts").get("socketio")
        self.application = application

        self._opts = {
            "host": self.config.get("host"),
            "port": self.config.get("port"),
        }

        self._rooms = []
        self._flags = {}

        self.uid = "communicator"

        if "client" in self._opts and self._opts["client"] is not None:
            self._client = self._opts["client"]
        else:
            self._client = self._createClient()

        self._key = self._opts.get("key", "socket.io")

    # Limit emission to a certain `room`.
    def In(self, *room):
        self._rooms.append(room)
        return self

    # Limit emission to a certain `room`.
    def To(self, *room):
        return self.In(room)

    # Limit emission to certain `namespace`.
    def Of(self, nsp):
        self._flags["nsp"] = nsp
        return self

    # Send the packet.
    def Emit(self, *args):
        packet = {}
        extras = {}

        packet["data"] = args
        packet["type"] = self.BINARY_EVENT if self._hasBin(args) else self.EVENT

        # set namespace to packet
        if "nsp" in self._flags:
            packet["nsp"] = self._flags["nsp"]
            del self._flags["nsp"]
        else:
            packet["nsp"] = "/"

        extras["flags"] = self._flags if len(self._flags) > 0 else ""

        rooms = self._getRooms()
        extras["rooms"] = rooms if len(rooms) > 0 else ""

        if extras["rooms"]:
            for room in rooms:
                chn = "#".join((self._key, packet["nsp"], room, ""))
                self._client.publish(chn, msgpack.packb([self.uid, packet, extras]))
        else:
            chn = "#".join((self._key, packet["nsp"], ""))
            self._client.publish(chn, msgpack.packb([self.uid, packet, extras]))

        self._flags = {}
        self._rooms = []

    # Makes [[1,2],3,[4,[5,6]]] into an iterator of [1,2,3,4,5,6]
    def _flatten(self, root):
        if isinstance(root, (list, tuple)):
            for element in root:
                for e in self._flatten(element):
                    yield e
        else:
            yield root

    # Get a list of unique rooms
    def _getRooms(self):
        return list(set(self._flatten(self._rooms)))

    # Not implemented yet
    def _hasBin(self, param):
        return False

    # Create a redis client from a `host:port` uri string.
    def _createClient(self):
        if "host" not in self._opts:
            raise Exception("Missing redis `host`")
        if "port" not in self._opts:
            raise Exception("Missing redis `port`")

        kwargs = {
            "host": self._opts["host"],
            "port": self._opts["port"],
        }

        if "password" in self._opts:
            kwargs["password"] = self._opts["password"]

        return redis.StrictRedis(**kwargs)

    def pubsub(self):
        return self._client.pubsub()

    def clients(self):
        client_keys = self._client.keys(pattern="mbroadcast:users:*")
        return [self.client(key) for key in client_keys]

    def client(self, id):
        client_data = self._client.hmget(id, "userID", "address", "sessionId", "connected")
        if client_data is None:
            return None

        userID, address, sessionID, connected = client_data

        userID = userID.decode("utf-8") if userID is not None else None
        address = address.decode("utf-8") if address is not None else None
        sessionID = sessionID.decode("utf-8") if sessionID is not None else None
        connected = connected.decode("utf-8") if connected is not None else False

        return SocketClient(userID, address, sessionID, connected == "true")

    def authenticate(self):
        return True
