from hobbyrpc import Server

rpc = Server()

class User:
    def __init__(self, name):
        self.name = name

@rpc.auth
def find_user(token):
    if token == 'ValidToken':
        return User('A')

@rpc.fun
class CurrentUser:
    def call(self):
        return self.user.__dict__
