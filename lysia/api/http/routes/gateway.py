from ....api.http.route import Route


def get_gateway() -> Route:
    return Route("GET", "/gateway")


def get_gateway_bot() -> Route:
    return Route("GET", "/gateway/bot")
