import os
from urllib import urlencode

from social_core.backends.oauth import BaseOAuth2


class ShikimoriOAuth2(BaseOAuth2):
    """GitHub OAuth authentication backend"""

    name = "shikimori"
    AUTHORIZATION_URL = os.getenv("SHIKI_AUTH_URL")
    ACCESS_TOKEN_URL = os.getenv("SHIKI_ACCESS_TOKEN_ENDPOINT")
    ACCESS_TOKEN_METHOD = os.getenv("SHIKI_ACCESS_TOKEN_METHOD")
    SCOPE_SEPARATOR = ","
    EXTRA_DATA = [("id", "id"), ("expires", "expires")]

    def get_user_details(self, response):
        """Return user details from Shikimori account.
        
        Args:
            response: response with data of user

        Returns:
            dict: user's data
        """
        return {
            "username": response.get("login"),
            "email": response.get("email") or "",
            "first_name": response.get("name"),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service.
        
        Args:
            access_token: API access token
            args: additional params
            kwargs: additional params

        Returns:
            dict: User's data
        """
        url = "https://api.github.com/user?" + urlencode({"access_token": access_token})
        return self.get_json(url)
