import pytest

pytest_plugins = [
    "tests.Client.fixtures.coffeerpc_server",
]

@pytest.fixture(scope="session", autouse=True)
def run_before_suite():
    # Code here runs BEFORE the entire test suite starts
    print("\n[Setup] Initializing global resources...")
    
    yield
    
    # Code here runs AFTER the entire test suite finishes
    print("\n[Teardown] Cleaning up global resources...")
