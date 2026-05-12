import pytest
from tests.helpers.coffeerpc import ensure_coffeerpc_exists

@pytest.fixture(scope="session", autouse=True)
def run_before_suite():
    ensure_coffeerpc_exists()
    
    yield
    
    # Code here runs AFTER the entire test suite finishes
    print("\n[Teardown] Cleaning up global resources...")
