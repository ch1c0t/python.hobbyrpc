from hobbyrpc import Server

CORS = {
    'methods': 'GET, POST, OPTIONS',
    'headers': 'Authorization, Content-Type, Content-Length',
    'max_age': '80000',
}

rpc = Server(
    CORS=CORS,
)

@rpc.fun
class SomeFunction:
    def call(self):
        return ['custom', 'headers']
