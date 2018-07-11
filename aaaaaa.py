import os
from pathlib import Path

if __name__ == "__main__":
    directory = Path(__file__).parent.parent.resolve() #pylint: disable=no-member
    if "VIRTUAL_ENV" in os.environ:
        pybin = directory / "bin" / "python"
    else:
        pybin = "/usr/bin/python"

    print(pybin)