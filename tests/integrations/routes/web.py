from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/users", "WelcomeController@users"),
    Route.get("/broadcast", "WelcomeController@broadcast"),
]
