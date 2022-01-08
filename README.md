#### Project description

**What is Minio-Driver?**

It's an extra broadcast driver support for Minio in masonite 4, it extends default masonite broadcast driver to support SocketIO.

**Setup**

Install package using pip:

```shell
pip install masonite-socketio-driver
```

Add provider inside config/providers.py.

```python
from masonite_socketio_driver.masonite_socketio_provider import MasoniteSocketioProvider

PROVIDERS = [
    ...,
    # Application Providers
    MasoniteSocketioProvider,
]
```

**Driver Config**
Add following configuration inside config/broadcast.py after `"pusher": {...},`

```python
"pusher": {...},
"socketio": {
    "driver": "socketio",
    "host": env("BROADCAST_HOST", "localhost"),
    "port": env("BROADCAST_PORT", "6379")
},
```

Add following keys in `.env`.

```shell
BROADCAST_HOST=
BROADCAST_PORT=
```

Update the broadcast driver value to `socketio` in `.env`

```shell
BROADCAST_DRIVER=socketio
```

**Example**

```python
from masonite.controllers import Controller
from masonite.broadcasting import Broadcast

class YourController(Controller):

    def your_function(self, broadcast: Broadcast):
        broadcast_data = {
            "message": "Hello World"
        }
        broadcast.channel(["channel-name"], "event-name", broadcast_data)
```
