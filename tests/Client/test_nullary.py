from hobbyrpc import Client

def test_nullary_call(tcp_server):
    call = Client(
        address='http://127.0.0.1:8080',
    )

    string = call('Version')

    assert string == '2.7.0'
