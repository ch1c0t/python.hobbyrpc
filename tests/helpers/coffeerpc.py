from pathlib import Path
from subprocess import run

coffee_path = Path("~/sources/coffee").expanduser()
coffeerpc_path = coffee_path / 'coffee.rpc'

def ensure_coffeerpc_exists():
    coffee_path.mkdir(parents=True, exist_ok=True)

    if not coffeerpc_path.is_dir():
        run(
            ['git', 'clone', 'https://github.com/ch1c0t/coffee.rpc'],
            cwd=coffee_path,
            check=True,
        )

        run(
            ['npm', 'install'],
            cwd=coffeerpc_path,
            check=True,
        )
