from hobbyrpc import Client

def test_nullary_call(coffeerpc_server):
    call = Client(
        address=coffeerpc_server.address,
    )

    string = call('Version')

    assert string == '2.7.0'
