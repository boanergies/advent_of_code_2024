from pathlib import Path
import typer
from typing_extensions import Annotated

import re

REGEX = r"mul\((?P<left>\d*),(?P<right>\d*)\)"


def multiply(x: str, y: str):
    return int(x) * int(y)


def main(
    input_data: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ]
):
    total = 0
    with input_data.open() as fin:
        data = fin.read()
        for match in re.finditer(REGEX, data):
            total += multiply(*match.groups())
    print(total)


if __name__ == "__main__":
    typer.run(main)
