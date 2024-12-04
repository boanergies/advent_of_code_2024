from pathlib import Path
import typer
from typing_extensions import Annotated


def main(
    input_data: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ]
):
    list_1 = list()
    list_2 = list()
    with input_data.open() as fin:
        for line in fin:
            num1, num2 = map(int, line.split())
            list_1.append(num1)
            list_2.append(num2)
    list_1.sort()
    list_2.sort()
    print(sum([abs(a - b) for a, b in zip(list_1, list_2)]))


if __name__ == "__main__":
    typer.run(main)
