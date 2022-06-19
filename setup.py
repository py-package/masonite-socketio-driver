from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="masonite_socketio_driver",
    version='0.1.7',
    author="Yubaraj Shrestha",
    author_email="companion.krish@outlook.com",
    description="Socket IO Broadcast Driver for Masonite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yubarajshrestha/masonite-socketio-driver",
    project_urls={
        "Bug Tracker": "https://github.com/yubarajshrestha/masonite-socketio-driver/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Masonite",
    ],
    packages=["masonite_socketio_driver"],
    package_dir={"masonite_socketio_driver": "src"},
    install_requires=[
        'masonite>=4.0,<5.0',
        'socket.io-emitter',
    ],
    license="MIT",
    keywords=["masonite", "socket-io", "broadcast", "masonite-socket-io-broadcast-driver"]
)
