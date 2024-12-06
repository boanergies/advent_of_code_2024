from pathlib import Path
import typer
from typing_extensions import Annotated

import re

REGEX = r"do\(\)|don't\(\)|mul\((?P<left>\d*),(?P<right>\d*)\)"


def multiply(x: str, y: str):
    return int(x) * int(y)


def main(
    input_data: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ]
):
    total = 0
    do_multi = True
    with input_data.open() as fin:
        data = fin.read()
        for text in re.finditer(REGEX, data):
            match text.group(0):
                case "do()":
                    do_multi = True
                case "don't()":
                    do_multi = False
                case _:
                    if do_multi:
                        total += multiply(*text.groups())
    print(total)


if __name__ == "__main__":
    typer.run(main)
