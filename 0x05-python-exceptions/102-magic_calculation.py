#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Value of 'i' exceeds 'a'")
            else:
                result += a ** b / i
        except ValueError as ve:
            result = b + a
            break
    return result
