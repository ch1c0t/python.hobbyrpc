from hobbyrpc import Server

rpc = Server()

@rpc.fun
class Echo:
    def call(self):
        return self.input
