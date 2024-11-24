# authentication.py
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from .models import CustomToken

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None

        try:
            token = token.split(' ')[1]
        except IndexError:
            raise AuthenticationFailed("Invalid token format")

        try:
            custom_token = CustomToken.objects.get(token=token)
            student = custom_token.student
            return (student, None)
        except CustomToken.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        return None
