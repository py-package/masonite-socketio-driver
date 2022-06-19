"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.broadcasting import Broadcast


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, broadcast: Broadcast):
        return view.render("welcome")

    def broadcast(self, view: View, broadcast: Broadcast):
        broadcast_data = {"message": "Hello World"}
        broadcast.channel(["default"], "welcome", broadcast_data)
        return {"hello": "world!"}
