from masonite.environment import env


BROADCASTS = {
    "default": "socketio",
    "pusher": {
        "driver": "pusher",
        "client": env("PUSHER_CLIENT"),
        "app_id": env("PUSHER_APP_ID"),
        "secret": env("PUSHER_SECRET"),
        "cluster": env("PUSHER_CLUSTER"),
        "ssl": False,
    },
    "socketio": {
        "driver": "socketio",
        "host": env("BROADCAST_HOST", "localhost"),
        "port": env("BROADCAST_PORT", "6379")
    },
}
