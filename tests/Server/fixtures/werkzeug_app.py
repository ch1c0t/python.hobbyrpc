from pathlib import Path

import pytest
from xprocess import ProcessStarter

@pytest.fixture(
    params=['tcp', 'unix_socket'],
)
def werkzeug_app(xprocess, request, tmp_path_factory):
    match request.param:
        case 'tcp':
            address = 'http://127.0.0.1:8000'
            bind_address = address.split('/')[-1]
        case 'unix_socket':
            socket_dir = tmp_path_factory.mktemp("uds")
            socket_path = str(socket_dir / "werkzeug_app.socket")
            address = socket_path
            bind_address = 'unix:' + address

    class Starter(ProcessStarter):
        # The command to start your process
        args = [
            'uv', 'run', 'gunicorn',
            '--bind', bind_address,
            'werkzeug_json:application',
        ]
        timeout = 3
        popen_kwargs = {
            'cwd': f'{Path.cwd()}/examples',
        }

        # Define how xprocess knows the process has started
        pattern = "Control socket listening at"

    # Start the process
    xprocess.ensure(request.fixturename, Starter)

    process = xprocess.getinfo(request.fixturename)
    process.transport = request.param
    process.address = address

    yield process

    process.terminate()
