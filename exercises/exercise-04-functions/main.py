"""Exercise 4: Working with functions and modules."""

from helper import (
    count_letter_cases,
    print_even_numbers,
    print_youngest_employee,
)


EMPLOYEES = [
    {
        "name": "Tina",
        "age": 30,
        "birthday": "1990-03-10",
        "job": "DevOps Engineer",
    },
    {
        "name": "Tim",
        "age": 35,
        "birthday": "1985-02-21",
        "job": "Developer",
    },
]

NUMBERS = [1, 2, 3, 4, 5, 6, 8, 11, 14, 20]


def main() -> None:
    print_youngest_employee(EMPLOYEES)

    text = "DevOps Engineering With Python"
    uppercase, lowercase = count_letter_cases(text)

    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")

    print_even_numbers(NUMBERS)


if __name__ == "__main__":
    main()