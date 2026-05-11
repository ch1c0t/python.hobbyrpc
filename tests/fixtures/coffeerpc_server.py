import os
from pathlib import Path

import pytest
from xprocess import ProcessStarter

coffeerpc_path = f'{Path.home()}/sources/coffee/coffee.rpc/bin/coffee.rpc'

@pytest.fixture(
    params=['tcp', 'unix_socket'],
)
def coffeerpc_server(xprocess, request, tmp_path_factory):
    match request.param:
        case 'tcp':
            address = 'http://127.0.0.1:8080'
        case 'unix_socket':
            socket_dir = tmp_path_factory.mktemp("uds")
            socket_path = str(socket_dir / "coffeerpc.socket")
            address = socket_path

    class Starter(ProcessStarter):
        # The command to start your process
        args = [coffeerpc_path, ]
        
        match request.param:
            case 'tcp':
                env = {
                    **os.environ,            # Keep existing system env vars
                    "TCP_HOST": "127.0.0.1", # Add your custom variable
                    "TCP_PORT": "8080",
                }
            case 'unix_socket':
                env = {
                    **os.environ,            # Keep existing system env vars
                    "SOCKET_PATH": socket_path,
                }
        
        # Define how xprocess knows the process has started
        pattern = "Listening on"

    # Start the process
    xprocess.ensure("coffeerpc_server", Starter)

    process = xprocess.getinfo("coffeerpc_server")
    process.transport = request.param
    process.address = address

    yield process

    process.terminate()
