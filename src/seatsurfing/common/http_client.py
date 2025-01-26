import logging

logger = logging.getLogger(__name__)


class SeatsurfingClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
