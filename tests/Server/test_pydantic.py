import pytest
from hobbyrpc import Client
from hobbyrpc.client.exceptions import BadRequest

def test_BaseModel_happy_path(pydantic_rpc):
    call = Client(
        address=pydantic_rpc.address,
    )

    result = call(
        'BaseModelFunction',
        first='first string',
        second='second string',
    )

    assert result == {
        'first': 'first string',
        'second': 'second string',
    }

def test_that_it_raises_an_error_when_not_all_required_fields_were_passed(pydantic_rpc):
    call = Client(pydantic_rpc.address)
    with pytest.raises(BadRequest):
        call(
            'BaseModelFunction',
            first='first string',
    )

def test_that_it_raises_an_error_when_a_value_of_a_wrong_type_was_passed(pydantic_rpc):
    call = Client(pydantic_rpc.address)
    with pytest.raises(BadRequest):
        call(
            'BaseModelFunction',
            first='first string',
            second=2,
    )

def test_field_accessors(pydantic_rpc):
    call = Client(
        address=pydantic_rpc.address,
    )

    result = call(
        'FieldAccessors',
        first='first string',
        second='second string',
    )

    assert result == 'first string and second string'

def test_BaseModel_json_dump(pydantic_rpc):
    call = Client(
        address=pydantic_rpc.address,
    )

    result = call(
        'BaseModelResponse',
    )

    assert result == {
        'name': 'A',
    }
