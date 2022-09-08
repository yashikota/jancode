def calculation(number, length) -> int:
    """Calculation Method
    1. Add even-digit numbers and multiply by 3.
    2. Add odd-numbered digits (excluding the last digit, which is the check digit).
    3. Add even-digit and odd-digit numbers and look at the 1's in the value.
    4. Subtract a number to the first place from 10 (If the number obtained in 3 is 0, the check digit is 0).
    """

    # 1
    even_number: int = 0
    for i in range(1, length, 2):
        even_number += int(number[i])
    even_number *= 3

    # 2
    odd_number: int = 0
    for i in range(0, length - 1, 2):
        odd_number += int(number[i])

    # 3
    ones_place: int = (even_number + odd_number) % 10

    # 4
    if ones_place == 0:
        calculated_checkdigit: int = 0
    else:
        calculated_checkdigit = 10 - ones_place

    return calculated_checkdigit


def check(number: str, length: int) -> bool:
    """Check if the entered checkdigit matches the calculated checkdigit"""
    input_checkdigit: int = int(number[length - 1])
    if input_checkdigit == calculation(number, length):
        return True
    else:
        return False
