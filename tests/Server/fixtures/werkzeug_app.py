import pytest

from tests.helpers.rpc_fixture import rpc_fixture

@pytest.fixture(
    params=['tcp', 'unix_socket'],
)
@rpc_fixture
def werkzeug_app(xprocess, request, tmp_path_factory):
    pass
