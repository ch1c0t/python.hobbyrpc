from .fun import change
from .logger import logger

class Server:
    def __init__(self, logger=logger):
        self.functions = {}
        self.logger = logger

    def auth(self, fn):
        self.auth_is_required = True
        self.find_user = fn

    def is_auth_required(self):
        if hasattr(self, 'auth_is_required'):
            return getattr(self, 'auth_is_required')

    def fun(self, cl):
        change(cl)

        instance = cl()
        self.functions[cl.__name__] = instance
        return instance

from .call import call
Server.__call__ = call
