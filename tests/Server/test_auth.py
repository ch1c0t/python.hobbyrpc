import pytest
from hobbyrpc import Client
from hobbyrpc.client.exceptions import BadRequest, Forbidden

def test_user_accessor(auth_rpc):
    call = Client(
        address=auth_rpc.address,
        token='ValidToken',
    )

    result = call(
        'CurrentUser',
    )

    assert result == {
        'name': 'A',
    }

def test_that_it_fails_when_no_token_was_passed(auth_rpc):
    call = Client(auth_rpc.address)
    with pytest.raises(Forbidden):
        call('CurrentUser')

def test_that_it_fails_when_an_invalid_token_was_passed(auth_rpc):
    call = Client(
        address=auth_rpc.address,
        token='InvalidToken',
    )

    with pytest.raises(Forbidden):
        call('CurrentUser')
