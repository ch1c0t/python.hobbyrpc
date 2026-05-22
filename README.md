## Introduction

It is a Python package to make [Hobby-RPC][hobby_rpc] clients and servers.

It depends on:

- [Werkzeug][werkzeug]
- [Pydantic][pydantic]

To install:

```
uv add hobbyrpc
```

## Client

A usage example:

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

output = call('SomeNullaryFunction')
output = call('SomeUnaryFunction', **input)

# a call to Compile that compiles CoffeeScript code to JavaScript
output = call(
    'Compile',
    code='answer = 42',
    bare=True,
)
```

`input` and `output` are Python objects serializable to and deserializable from JSON.

## Server

Not implemented yet.

[hobby_rpc]: https://github.com/ch1c0t/hobby-rpc.protocol
[wergzeug]: https://palletsprojects.com/projects/werkzeug
[pydantic]: https://pydantic.dev/docs/validation/latest/get-started
