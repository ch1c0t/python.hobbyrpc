from hobbyrpc import Server

rpc = Server()

@rpc.fun
class ListNames:
    def call(self):
        return ['default']
