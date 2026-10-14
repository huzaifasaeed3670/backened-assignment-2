def remove_duplicates(numbers):
    """Return the numbers without duplicates, preserving their original order."""
    return list(dict.fromkeys(numbers))


def find_average(numbers):
    """Return the arithmetic mean of the numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


def multiply_by_scalar(numbers, scalar):
    """Return a new list with every number multiplied by scalar."""
    return [number * scalar for number in numbers]


if __name__ == "__main__":
    values = [2, 4, 2, 6, 4, 8]
    scalar = 3

    print("Original list:", values)
    print("Without duplicates:", remove_duplicates(values))
    print("Average:", find_average(values))
    print("Multiplied by", scalar, ":", multiply_by_scalar(values, scalar))