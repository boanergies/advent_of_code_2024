from pathlib import Path
import typer
from typing_extensions import Annotated


def main(
    input_data: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ]
):
    key_list = list()
    value_list = dict()
    with input_data.open() as fin:
        for line in fin:
            num1, num2 = map(int, line.split())
            key_list.append(num1)
            try:
                value_list[num2] += 1
            except KeyError:
                value_list[num2] = 1
    print(sum([num * value_list[num] if num in value_list else 0 for num in key_list]))


if __name__ == "__main__":
    typer.run(main)
