from masonite.environment import LoadEnvironment, env
from masoniteorm.connections import ConnectionResolver

#  Loads in the environment variables when this page is imported.
LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""
DATABASES = {
    "default": env("DB_CONNECTION", "sqlite"),
    "sqlite": {
        "driver": "sqlite",
        "database": env("SQLITE_DB_DATABASE", "masonite.sqlite3"),
        "prefix": "",
        "log_queries": env("DB_LOG"),
    },
    "mysql": {
        "host": "127.0.0.1",
        "driver": "mysql",
        "database": "masonite_permission",
        "user": "meyubaraj",
        "password": "MDB@123#go",
        "port": 3306,
        "prefix": "",
        "grammar": "mysql",
        "options": {
            "charset": "utf8mb4",
        },
        "log_queries": env("DB_LOG"),
    },
    "postgres": {
        "host": "127.0.0.1",
        "driver": "postgres",
        "database": "masonite_permission",
        "user": "meyubaraj",
        "password": "MDB@123#go",
        "port": 5432,
        "prefix": "",
        "grammar": "postgres",
        "log_queries": env("DB_LOG"),
    },
    "mssql": {
        "driver": "mssql",
        "host": env("MSSQL_DATABASE_HOST"),
        "user": env("MSSQL_DATABASE_USER"),
        "password": env("MSSQL_DATABASE_PASSWORD"),
        "database": env("MSSQL_DATABASE_DATABASE"),
        "port": env("MSSQL_DATABASE_PORT"),
        "prefix": "",
        "log_queries": env("DB_LOG"),
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)
