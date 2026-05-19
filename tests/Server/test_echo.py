import pytest
from hobbyrpc import Client
from hobbyrpc.client.exceptions import BadRequest

def test_receiving_a_list(echo_rpc):
    call = Client(
        address=echo_rpc.address,
    )

    list = call(
        'Echo',
        ['any', 'input'],
    )

    assert list == [
        'any',
        'input',
    ]
