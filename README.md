## Introduction

It is a Python package to make [Hobby-RPC][hobby_rpc] clients and servers.

It depends on:

- [Werkzeug][werkzeug]
- [Pydantic][pydantic]

To install:

```
uv add hobbyrpc
```

## Server

To create a server:

```python
from hobbyrpc import Server

rpc = Server()

@rpc.fun
class FunctionName:
    def call(self):
        return 'any object serializable to JSON'

@rpc.fun
class OtherFunctionName:
    def call(self):
        return ['any', 'object', 'serializable', 'to', 'JSON']
```

In the above example, `rpc` is a WSGI application.
With [multiple options for deployment][werkzeug.deployment].

To provide it via a TCP socket with [Gunicorn][gunicorn]:

```zsh
uv run gunicorn --bind '127.0.0.1:8000' 'module_name:rpc'
```

Via Unix socket:

```zsh
uv run gunicorn --bind unix:/tmp/rpc.socket 'module_name:rpc'
```

### `self.input`

The raw input of a function can be accessed via `self.input`.
Here is an example of a function echoing its input back to the client:

```python
@rpc.fun
class Echo:
    def call(self):
        return self.input
```

### Pydantic

#### Validation

In most cases, it is advisable to rely on [Pydantic][pydantic] for validating input
instead of parsing `self.input` yourself.

To do so, input fields shall be passed as class annotations. Like so:

```python
@rpc.fun
class ContrivedConcatenation:
    first: str
    second: str

    def call(self):
        # self.pydantic provides an instance of Pydantic's BaseModel
        # its fields are available as self attributes too:
        #   self.pydantic.first == self.first
        #   self.pydantic.second == self.second
        return f'{self.first} and {self.second}'
```

If a client does not pass an input with all required fields
or pass a value of a wrong type, the server responds with
[400 Bad Request][BadRequest].

#### Output

Instances of Pydantic's BaseModel can also be used as outputs
of RPC functions:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'

@rpc.fun
class SomeUser:
    def call(self):
        user = User(id=1)
        return user
```

### `@rpc.auth`

By default, any client is allowed to call the functions.
To restrict that, use `@rpc.auth` decorator to define `find_user`
function as follows:

```python
@rpc.auth
def find_user(token):
    if token == 'ValidToken':
        return User(id=1)
```

`find_user` should be a function that takes one argument, `token` string.
`token` is what clients are supposed to pass in [the Authorization header][Authorization].

If `find_user` returns a falsy value or raises en error,
the server responds with [403 Forbidden][Forbidden].

If `find_user` returns something else,
the server will assume it is something that represents the current user
and will make it available as `self.user`:

```python
@rpc.fun
class CurrentUser:
    def call(self):
        return self.user
```

### CORS

By default, the server sets permissive CORS headers(`Access-Control-Allow-Origin: *`)
for requests from any origin. To restrict that, pass a list of allowed domains in
`origins` as follows:

```python
from hobbyrpc import Server

CORS = {
    'origins': [
        'https://allowed.domain',
        'https://www.allowed.domain',
    ]
}

rpc = Server(
    CORS=CORS,
)
```

## Client

Initialize a `Client` by passing it an `address` and, optionally, a `token` too.
Like so:

```python
from hobbyrpc import Client

# via tcp
call = Client(
    address='http://127.0.0.1:8080',
    token="authorization token",
)

# or via unix socket
call = Client(
    address='/tmp/path/to/rpc.socket',
    token="authorization token",
)
```

Call functions remotely. Like so:

```python
input = {
    'first': 1,
    'second': 2,
}

output = call('SomeUnaryFunction', **input)
output = call('SomeNullaryFunction')

# a call to Compile that compiles CoffeeScript to JavaScript
output = call(
    'Compile',
    code='answer = 42',
    bare=True,
)
```

`input` and `output` are Python objects serializable to and deserializable from JSON.

## Development

`uv run pytest` to run the tests.

[hobby_rpc]: https://github.com/ch1c0t/hobby-rpc.protocol
[werkzeug]: https://palletsprojects.com/projects/werkzeug
[werkzeug.deployment]: https://werkzeug.palletsprojects.com/en/stable/deployment/
[pydantic]: https://pydantic.dev/docs/validation/latest/get-started
[gunicorn]: https://gunicorn.org/
[BadRequest]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
[Authorization]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
[Forbidden]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
