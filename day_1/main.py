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
            num1, num2 = line.strip().split("   ")
            list_1.append(int(num1))
            list_2.append(int(num2))
    list_1.sort()
    list_2.sort()
    print(list_1)
    print(list_2)
    distance = 0
    for value1, value2 in zip(list_1, list_2):
        distance += abs(value1 - value2)
    print(distance)


if __name__ == "__main__":
    typer.run(main)
