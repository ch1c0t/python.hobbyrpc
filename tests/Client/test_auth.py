import pytest
from hobbyrpc import Client
from hobbyrpc.client.exceptions import Forbidden

def test_auth_token(coffeerpc_server_with_auth):
    call = Client(
        address=coffeerpc_server_with_auth.address,
        token="ValidTokenToTestPythonClient",
    )

    string = call('User')

    assert string == 'a string to test that auth works'

def test_auth_forbidden_without_token(coffeerpc_server_with_auth):
    call = Client(
        address=coffeerpc_server_with_auth.address,
    )

    with pytest.raises(Forbidden):
        call('User')
