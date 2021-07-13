from argparse import ArgumentParser, ArgumentTypeError, Namespace
from sys import argv


def check_errors(str: str) -> str:
    for a in range(0, len(str)):
        n: int = ord(str[a])
        if n != ord("*") and (n > ord("9") or n < ord("0")):
            raise ArgumentTypeError
    return str


def parse_args() -> Namespace:
    parser = ArgumentParser(usage="%(prog)s [num den]")
    parser.add_argument(
        "numerator",
        nargs=1,
        type=check_errors,
        help="polynomial numerator defined by its coefficients",
    )
    parser.add_argument(
        "denominator",
        nargs=1,
        type=check_errors,
        help="polynomial denominateur defined by its coefficients",
    )
    parser.add_argument(
        "mutiplication",
        nargs="*",
        type=check_errors,
        help="multiplication symbol between numerator and denominator",
    )
    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)
    if (len(argv) - 1) % 2 != 0:
        print("Missing argument")
        exit(84)
    return args
