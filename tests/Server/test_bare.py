from hobbyrpc import Client

def test_receiving_a_list(bare_rpc):
    call = Client(
        address=bare_rpc.address,
    )

    list = call('ListNames')

    assert list == ['default']
