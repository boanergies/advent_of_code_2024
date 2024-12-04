from collections.abc import Callable
from pathlib import Path
import typer
from typing_extensions import Annotated


def rule(comp_func: Callable, num1, num2):
    return comp_func(num1, num2) and (1 <= abs(num1 - num2) <= 3)


def is_safe(comp_func: Callable, numbers: list):
    for i in range(len(numbers) - 1):
        if not rule(comp_func, numbers[i], numbers[i + 1]):
            return i + 1
    return len(numbers)


def error_module(comp_func: Callable, numbers: list):
    # remove at least one element
    if (error_index := is_safe(comp_func, numbers)) != len(numbers):
        new_list_1 = list(numbers)
        new_list_1.pop(error_index)
        new_list_2 = list(numbers)
        new_list_2.pop(error_index - 1)
        return is_safe(comp_func, new_list_1) == len(new_list_1) or is_safe(
            comp_func, new_list_2
        ) == len(new_list_2)
    return True


def is_increasing(numbers: list):
    return error_module(lambda x, y: x < y, numbers)


def is_decreasing(numbers: list):
    return error_module(lambda x, y: x > y, numbers)


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
