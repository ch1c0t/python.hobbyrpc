import pytest
from pathlib import Path


@pytest.fixture(scope="session", autouse=True)
def run_before_suite():
    # Code here runs BEFORE the entire test suite starts
    print("\n[Setup] Initializing global resources...")

    path = Path("~/sources/coffee").expanduser()
    path.mkdir(parents=True, exist_ok=True)
    
    yield
    
    # Code here runs AFTER the entire test suite finishes
    print("\n[Teardown] Cleaning up global resources...")
