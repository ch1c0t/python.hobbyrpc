import pytest

pytest_plugins = [
    "tests.Client.fixtures.coffeerpc_server",
    "tests.Client.fixtures.coffeerpc_server_with_auth",
]
