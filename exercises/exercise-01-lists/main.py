"""Exercise 1: Working with lists."""

MY_LIST = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]


def print_values_greater_than_or_equal_to_ten() -> None:
    """Print each element greater than or equal to 10."""
    for number in MY_LIST:
        if number >= 10:
            print(number)


def create_values_greater_than_or_equal_to_ten() -> list[int]:
    """Return all values greater than or equal to 10."""
    return [number for number in MY_LIST if number >= 10]


def filter_values_greater_than_user_number(number: float) -> list[int]:
    """Return list elements greater than a user-provided number."""
    return [value for value in MY_LIST if value > number]


def main() -> None:
    print("Elements greater than or equal to 10:")
    print_values_greater_than_or_equal_to_ten()

    filtered_list = create_values_greater_than_or_equal_to_ten()
    print(f"\nNew list: {filtered_list}")

    while True:
        user_input = input(
            "\nEnter a number to filter the list, or type 'exit' to quit: "
        ).strip()

        if user_input.lower() == "exit":
            print("Exercise finished.")
            break

        try:
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        result = filter_values_greater_than_user_number(number)
        print(f"Values greater than {number:g}: {result}")
        break


if __name__ == "__main__":
    main()