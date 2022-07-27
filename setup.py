from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="masonite-socketio-driver",
    version='2.0.5',
    packages=[
        "socketio_driver",
        "socketio_driver.config",
        "socketio_driver.drivers",
        "socketio_driver.providers"
    ],
    package_dir={"": "src"},
    description="Socket IO Broadcast Driver for Masonite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/py-package/masonite-socketio-driver",
    # Author details
    author="Yubaraj Shrestha",
    author_email="yubaraj@pypackage.com",
    project_urls={
        "Bug Tracker": "https://github.com/py-package/masonite-socketio-driver/issues",
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        # List package on masonite packages website
        "Framework :: Masonite",
    ],
    keywords=["masonite", "socket-io", "broadcast", "masonite-socket-io-broadcast-driver"],
    install_requires=["masonite>=4.0<5.0", 'socket.io-emitter', 'redis', 'msgpack'],
    license="MIT",
    extras_require={
        "dev": [
            "black",
            "flake8",
            "coverage",
            "pytest",
            "pytest-cov",
            "twine>=1.5.0",
            "wheel",
        ],
    },
    package_data={
        'templates/index.html': [],
    },
)
