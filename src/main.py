from pypflow import *


def square(x):
    return x**2


def add(x):
    return x + 10


def filter_odd(x):
    return x if x % 2 != 0 else None


if __name__ == "__main__":
    pipeline = pipe(square, add, filter_odd)

    input_data = 5

    output = pipeline(input_data)

    print(output)
