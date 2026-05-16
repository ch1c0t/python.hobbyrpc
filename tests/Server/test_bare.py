import pytest
from hobbyrpc import Client
from hobbyrpc.client.exceptions import BadRequest

def test_receiving_a_list(bare_rpc):
    call = Client(
        address=bare_rpc.address,
    )

    list = call('ListNames')

    assert list == ['default']

def test_calling_nonexistent_name(bare_rpc):
    call = Client(bare_rpc.address)

    with pytest.raises(BadRequest):
        call('NonexistentName')
