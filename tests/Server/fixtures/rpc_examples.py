from pathlib import Path
from tests.helpers.rpc_fixture import rpc_fixture

cwd = Path.cwd()

for file in cwd.glob('examples/*.py'):
    stem = file.stem
    globals()[stem] = rpc_fixture(stem)
