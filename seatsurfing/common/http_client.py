import logging
from urllib.parse import urlparse

import httpx

from seatsurfing.models.authentication import Jwt, PasswordLoginRequest

logger = logging.getLogger(__name__)


class SeatsurfingHttpClient:
    def __init__(self, base_url: str, *, username: str = None, password: str = None):
        self.__base_url = urlparse(base_url)
        self.__jwt: Jwt = None
        self.__client = httpx.Client(follow_redirects=True, base_url=base_url)

        # login if username/password provided.
        if username and password:
            self.__password_login(username, password)

    def __del__(self):
        self.__client.close()

    def __is_logged_in(self) -> bool:
        "Check if the client is logged in."
        # We can't check if it's actually a real URL, but we can check if it's empty at least.
        if not self.__base_url:
            return False

        if not self.__jwt:
            return False

        if not self.__client.headers.get("Authorization"):
            return False

        return True

    def __get(
        self, path: str, *, params: dict = None, headers: dict = None
    ) -> dict | list[dict] | None:
        if not self.__is_logged_in():
            return None

        r = self.__client.get(path, headers=headers, params=params)
        r.raise_for_status()
        return r.json()

    def __post(
        self, path: str, *, data: dict = None, params: dict = None, headers: dict = None
    ) -> dict | list[dict] | None:
        if not self.__is_logged_in():
            return None

        r = self.__client.post(path, data=data, headers=headers, params=params)
        r.raise_for_status()
        return r.json()

    def __put(
        self, path: str, *, data: dict = None, params: dict = None, headers: dict = None
    ) -> dict | list[dict] | None:
        if not self.__is_logged_in():
            return None

        r = self.__client.put(path, data=data, headers=headers, params=params)
        r.raise_for_status()
        return r.json()

    def __delete(
        self, path: str, *, params: dict = None, headers: dict = None
    ) -> dict | list[dict] | None:
        if not self.__is_logged_in():
            return None

        r = self.__client.delete(path, headers=headers, params=params)
        r.raise_for_status()
        return r.json()

    def __password_login(self, username: str, password: str) -> Jwt:
        """Authenticate using username and password, and update class http client with new bearer token."""
        logger.debug("Logging in using username/password: %s | %s", username, password)

        data = PasswordLoginRequest(email=username, password=password)

        url = f"{self.__base_url}/auth/login"
        # We don't use the class' client because this is an unauthenticated endpoint.
        r = httpx.post(url, data=data, follow_redirects=True)
        r.raise_for_status()
        jwt = Jwt.model_validate(r.json())

        logger.debug("Successfully retrieved JWT: %s", jwt)

        headers = {"Authorization": f"Bearer {jwt.access_token}"}
        self.__client.headers.update(headers)

        return jwt
