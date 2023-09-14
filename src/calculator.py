import typing


def calc(
        operator: str,
        val1: typing.Union[int, float],
        val2: typing.Union[int, float]
):
    if operator == "+":
        return val1 + val2

    if operator == "-":
        return val1 - val2

    if operator == "*":
        return val1 * val2

    if operator == "/":
        try:
            return val1 / val2
        except ZeroDivisionError:
            return 0
