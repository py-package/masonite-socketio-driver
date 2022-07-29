<p align="center">
    <img src="https://banners.beyondco.de/Masonite%20SocketIO%20Driver.png?theme=light&packageManager=pip+install&packageName=masonite-socketio-driver&pattern=charlieBrown&style=style_2&description=Driver+support+for+SocketIO+in+masonite+4.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-socketio-driver">
  <img alt="issues" src="https://img.shields.io/github/issues/py-package/masonite-socketio-driver">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/masonite-socketio-driver">
  <img alt="License" src="https://img.shields.io/github/license/py-package/masonite-socketio-driver">
  <a href="https://github.com/py-package/masonite-socketio-driver/stargazers"><img alt="star" src="https://img.shields.io/github/stars/py-package/masonite-socketio-driver" /></a>
  <img alt="downloads" src="https://img.shields.io/pypi/dm/masonite-socketio-driver?style=flat" />
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## SocketIO Driver

It's an extra broadcast driver support for SocketIO in masonite 4, it extends default masonite broadcast driver to support SocketIO.

**Masonite Broadcast Server and Client Library**
- [x] [Broadcast Server](https://github.com/py-package/masonite-broadcast-server)
- [x] [broadcast Client](https://github.com/py-package/masonite-broadcast-client)

**Setup**

Install package using pip:

```shell
pip install masonite-socketio-driver
```

Add provider inside config/providers.py.

```python
from socketio_driver.providers import SocketProvider

PROVIDERS = [
    ...,
    # Application Providers
    SocketProvider,
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

**Helpers**

List all connected clients:
    
```python
from socketio_driver.facades import Communicator

communicator.clients() # get list of connected clients
communicator.client(id='client-id') # get client by id, id is basically a socket.io session id
```