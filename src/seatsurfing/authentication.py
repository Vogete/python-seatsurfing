import httpx
import logging

from seatsurfing.models.authentication import JWTResponse, PasswordLoginRequest
from seatsurfing.common.http_client import SeatsurfingClient

logger = logging.getLogger(__name__)


class Authentication(SeatsurfingClient):
    """Online docs: https://seatsurfing.app/docs/rest-api#authentication"""

    def password_login(self, username: str, password: str) -> JWTResponse:
        """Authenticate using username and passowrd."""
        logger.debug("Logging in using username/password: %s | %s", username, password)

        data = PasswordLoginRequest(email=username, password=password)

        url = f"{self.base_url}/auth/login"
        r = httpx.post(url, data=data, follow_redirects=True)
        r.raise_for_status()

        jwt = JWTResponse.model_validate(r.json())

        logger.debug("Successfully retrieved JWT: %s", jwt)

        return jwt
