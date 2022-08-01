"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.broadcasting import Broadcast
from src.socketio_driver.facades import Communicator


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, broadcast: Broadcast):
        users = Communicator.clients()
        print(users)
        return view.render("welcome")

    def broadcast(self, view: View, broadcast: Broadcast):
        broadcast_data = {"message": "Hello World"}
        broadcast.channel(["default"], "welcome", broadcast_data)
        return {"hello": "world!"}
