"""Reusable helper functions for Exercise 4."""


def print_youngest_employee(employees: list[dict]) -> None:
    """Print the name and age of the youngest employee."""
    if not employees:
        print("No employees supplied.")
        return

    youngest = min(employees, key=lambda employee: employee["age"])

    print(
        f"Youngest employee: {youngest['name']} "
        f"({youngest['age']} years old)"
    )


def count_letter_cases(text: str) -> tuple[int, int]:
    """Return counts of uppercase and lowercase letters."""
    uppercase_count = 0
    lowercase_count = 0

    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


def print_even_numbers(numbers: list[int]) -> None:
    """Print all even values from the provided list."""
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(f"Even numbers: {even_numbers}")