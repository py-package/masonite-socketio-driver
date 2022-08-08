"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.broadcasting import Broadcast
from src.socketio_driver.facades import Communicator


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, broadcast: Broadcast):
        return view.render("welcome")

    def users(self):
        # Communicator.delete_all_clients()
        users = Communicator.clients()

        return {"users": [user.to_json() for user in users]}

    def broadcast(self, view: View, broadcast: Broadcast):
        broadcast_data = {"message": "Hello World"}
        users = Communicator.clients()
        for user in users:
            broadcast.driver("socketio").user(user).send("message", user.to_json())

        broadcast.channel(["mbroadcast"], "message", broadcast_data)
        return {"hello": "world!"}
