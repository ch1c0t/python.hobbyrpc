from .fun import change
from .auth import Auth
from .cors import CORS
from .post import POST
from .options import OPTIONS
from .logger import logger

class Server(Auth, CORS, POST, OPTIONS):
    def __init__(self, logger=logger, CORS={}):
        self.functions = {}
        self.logger = logger

        default_CORS = {
            'methods': 'POST, OPTIONS',
            'headers': 'Authorization, Content-Type',
            'max_age': '86400',
            'origins': '*',
        }
        self.CORS = { **default_CORS, **CORS }

    def fun(self, cl):
        change(cl)

        instance = cl()
        self.functions[cl.__name__] = instance
        return instance

from .call import call
Server.__call__ = call
