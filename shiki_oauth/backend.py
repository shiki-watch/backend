import os

from social_core.backends.oauth import BaseOAuth2


class ShikimoriOAuth2(BaseOAuth2):
    """GitHub OAuth authentication backend"""

    name = "shikimori"
    AUTHORIZATION_URL = os.getenv("SHIKI_AUTH_URL")
    ACCESS_TOKEN_URL = os.getenv("SHIKI_ACCESS_TOKEN_ENDPOINT")
    ACCESS_TOKEN_METHOD = os.getenv("SHIKI_ACCESS_TOKEN_METHOD")
    SCOPE_SEPARATOR = "+"

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

    def user_data(self, *args, **kwargs):
        """Loads user data from service.
        
        Args:
            args: additional params
            kwargs: additional params

        Returns:
            dict: User's data
        """
        url = "https://shikimori.one/api/users/whoami"
        return self.get_json(url)
