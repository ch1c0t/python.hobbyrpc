from .fun import change
from .auth import Auth
from .logger import logger

class Server(Auth):
    def __init__(self, logger=logger):
        self.functions = {}
        self.logger = logger

    def fun(self, cl):
        change(cl)

        instance = cl()
        self.functions[cl.__name__] = instance
        return instance

from .call import call
Server.__call__ = call
