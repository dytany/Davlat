"""A simple command-line calculator: addition, subtraction, multiplication, division."""

import operator
import sys

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(a: float, op: str, b: float) -> float:
    """Apply operation `op` to numbers `a` and `b`."""
    if op not in OPERATIONS:
        raise ValueError(f"unsupported operation: {op}")
    if op == "/" and b == 0:
        raise ZeroDivisionError("division by zero")
    return OPERATIONS[op](a, b)


def main(argv: list) -> int:
    if len(argv) != 4:
        print("Usage: python calc.py <number> <operation> <number>")
        print("Operations: + - * /")
        return 1

    try:
        a = float(argv[1])
        op = argv[2]
        b = float(argv[3])
        result = calculate(a, op, b)
    except (ValueError, ZeroDivisionError) as exc:
        print(f"Error: {exc}")
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))