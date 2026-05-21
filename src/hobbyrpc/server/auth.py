from .exceptions import Forbidden

class Auth:
    def auth(self, fn):
        self.auth_is_required = True
        self.find_user = fn

    def is_auth_required(self):
        if hasattr(self, 'auth_is_required'):
            return getattr(self, 'auth_is_required')

    def current_user(self, request):
        if self.is_auth_required():
            token = request.headers.get('Authorization')
            if not token:
                raise Forbidden

            user = self.find_user(token)
            if not user:
                raise Forbidden
        else:
            user = None

        return user
