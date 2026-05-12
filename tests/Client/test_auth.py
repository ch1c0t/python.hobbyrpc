from hobbyrpc import Client

def test_auth_token(coffeerpc_server_with_auth):
    call = Client(
        address=coffeerpc_server_with_auth.address,
        token="ValidTokenToTestPythonClient",
    )

    string = call('User')

    assert string == 'a string to test that auth works'
