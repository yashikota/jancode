import sys

import jancode.check_digit as checkdigit
import jancode.convert as convert
import jancode.property as property
import jancode.create_svg as svg


def check_digit(number: str, length: int) -> None:
    """Calculate the check digit"""
    if checkdigit.check(number, length):
        print("Check digit is correct.")
    else:
        print("Check digit is incorrect.")
        sys.exit()


def generate(number: int | str, path: str = ".") -> None:
    """Generate JAN code"""
    length, width, jancode_number, center_position, combi = property.set_property(
        str(number)
    )
    check_digit(str(number), length)
    binary_number: str = convert.binary(jancode_number, combi, center_position)

    # TODO: dubug
    print(binary_number)

    svg.create(binary_number, width, path, str(number))
