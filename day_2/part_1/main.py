from pathlib import Path
import typer
from typing_extensions import Annotated


def is_increasing(number: list):
    return all(
        number[i] < number[i + 1] and (1 <= abs(number[i] - number[i + 1]) <= 3)
        for i in range(len(number) - 1)
    )


def is_decreasing(number: list):
    return all(
        number[i] > number[i + 1] and (1 <= abs(number[i] - number[i + 1]) <= 3)
        for i in range(len(number) - 1)
    )


def main(
    input_data: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ]
):
    number_safe = 0
    with input_data.open() as fin:
        for line in fin:
            numbers = list(map(int, line.split()))
            if is_increasing(numbers) or is_decreasing(numbers):
                number_safe += 1
    print(number_safe)


if __name__ == "__main__":
    typer.run(main)
