
"""Lab 2.2 – Comprehensions and Transformations."""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return the square of each number."""
    return [x ** 2 for x in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only positive numbers."""
    return [x for x in numbers if x > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return squares of even numbers as a set."""
    return {x ** 2 for x in numbers if x % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dictionary mapping numbers to cubes."""
    return {x: x ** 3 for x in numbers}


if __name__ == "__main__":
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")
