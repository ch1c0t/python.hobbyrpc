from .fun import change

class Server:
    def __init__(self):
        self.functions = {}

    def fun(self, cl):
        change(cl)

        instance = cl()
        self.functions[cl.__name__] = instance
        return instance

from .call import call
Server.__call__ = call
