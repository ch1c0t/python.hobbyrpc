from hobbyrpc import Server

rpc = Server()

@rpc.fun
class BaseModelFunction:
    first: str
    second: str

    def call(self):
        return self.pydantic

@rpc.fun
class FieldAccessors:
    first: str
    second: str

    def call(self):
        return f'{self.first} and {self.second}'

from pydantic import BaseModel
class Response(BaseModel):
    name: str

@rpc.fun
class BaseModelResponse:
    def call(self):
        return Response(
            name='A',
        )
