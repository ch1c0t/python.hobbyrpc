class Server:
    def __init__(self):
        self.functions = {}

    def fun(self, cl):
        cl.__call__ = cl.call
        instance = cl()
        self.functions[cl.__name__] = instance
        return instance

from .call import call
Server.__call__ = call
