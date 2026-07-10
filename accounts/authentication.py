from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user_id = request.headers.get("X-User-Id")

        if not user_id:
            raise AuthenticationFailed("X-User-Id header is required.")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("Invalid User.")

        return (user, None)
        