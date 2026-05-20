from hobbyrpc import Server

rpc = Server()

@rpc.fun
class BaseModelFunction:
    first: str
    second: str

    def call(self):
        return self.pydantic
