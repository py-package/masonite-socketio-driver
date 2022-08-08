from masonite.controllers import Controller
from masonite.broadcasting import Broadcast
from masonite.request import Request
from masonite.response import Response


class BroadcastController(Controller):
    def authorize(self, request: Request, broadcast: Broadcast, response: Response):
        if not request.user():
            return response.json({"message": "unauthorized"}, 204)

        return broadcast.driver("socketio").authorize(
            request.input("channel_name"), request.input("socket_id"), request.user().id
        )
