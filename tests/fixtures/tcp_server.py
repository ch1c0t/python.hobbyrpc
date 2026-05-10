import os
from pathlib import Path

import pytest
from xprocess import ProcessStarter

coffeerpc_path = f'{Path.home()}/sources/coffee/coffee.rpc/bin/coffee.rpc'

@pytest.fixture
def tcp_server(xprocess):
    class Starter(ProcessStarter):
        # The command to start your process
        args = [coffeerpc_path, ]
        
        # Pass environment variables here
        env = {
            **os.environ,            # Keep existing system env vars
            "TCP_HOST": "127.0.0.1", # Add your custom variable
            "TCP_PORT": "8080",
        }
        
        # Define how xprocess knows the process has started
        pattern = "Listening on"

    # Start the process
    xprocess.ensure("tcp_server", Starter)
    yield

    xprocess.getinfo("tcp_server").terminate()
