from seatsurfing.booking import Booking


class Client:
    """Client to interact with Seatsurfing."""

    def __init__(self, base_url: str, username: str, password: str):
        self.booking = Booking(base_url, username=username, password=password)
