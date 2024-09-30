"""Median calculation module."""


def check(value):
    """Find the median of a list of values."""
    length_of_list = len(value)
    number = sorted(value)

    if not length_of_list:
        return None

    if not length_of_list % 2:
        return number[length_of_list // 2 - 1] / 2.0 + number[length_of_list // 2] / 2.0
    return number[length_of_list // 2]


def main():
    """Main function to calculate median from input values."""
    countable = int(input())
    number_list = []

    for _ in range(countable):
        number_list.append(float(input()))

    median = check(number_list)
    if median is not None:
        print(f"{median:.3f}")


main()
